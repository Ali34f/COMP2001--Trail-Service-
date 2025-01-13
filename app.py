from flask import Flask, request, jsonify, render_template, abort, make_response, redirect
from flask_restful import Api, Resource
from flask_cors import CORS
from flasgger import Swagger
from database_connection import get_db_connection
from crud_operations import create_trail, read_trail, update_trail, delete_trail
from authenticator import authenticate_user
import jwt
import datetime
import logging

# Initialize Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Initialize API and Swagger
api = Api(app)
swagger = Swagger(app, template_file="swagger.yml")

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Secret key for token generation
SECRET_KEY = "your_secret_key"

# Database connection
conn = get_db_connection()
if conn is None:
    raise ConnectionError("Database connection failed. Check your database settings.")

# Function to validate JWT tokens
def validate_token(auth_header):
    """Validates the JWT token from the Authorization header."""
    if not auth_header or not auth_header.startswith("Bearer "):
        abort(403, description="Unauthorized access")

    token = auth_header.split(" ")[1]
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        abort(401, description="Token has expired")
    except jwt.InvalidTokenError:
        abort(403, description="Invalid token")


# Function to generate JWT tokens
def generate_token(user_id, role):
    """Generates a JWT token for a user."""
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # PyJWT returns the token as a byte string, so decode it to a string
    return token if isinstance(token, str) else token.decode("utf-8")


@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": error.description}), 403

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": error.description}), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": error.description}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route("/")
def redirect_to_swagger():
    """Redirects the base route to Swagger UI."""
    return redirect("/apidocs")
@app.route("/auth", methods=["POST"])
def login():
    """Handles user login and returns a JWT token."""
    """
    ---
    tags:
      - Authentication
    summary: Authenticate User
    description: Authenticates the user and returns a JWT token.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login successful
        schema:
          type: object
          properties:
            message:
              type: string
            token:
              type: string
            role:
              type: string
      400:
        description: Email and password are required.
      401:
        description: Authentication failed.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"error": "Email and password are required."}), 400

    user = authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Authentication failed."}), 401

    token = generate_token(user["user_id"], user["role"])
    return jsonify({"message": "Login successful!", "token": token, "role": user["role"]})


# Resource: Trails
class TrailList(Resource):
    def get(self):
        """Fetches all trails."""
        """
        ---
        tags:
          - Trails
        summary: Get all trails
        responses:
          200:
            description: A list of trails
        """
        try:
            trails = []
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CW2.trails")
            rows = cursor.fetchall()
            for row in rows:
                trails.append({
                    "TrailID": row.TrailID,
                    "Trail_name": row.Trail_name,
                    "Trail_Summary": row.Trail_Summary,
                    "Trail_Description": row.Trail_Description,
                    "Difficulty": row.Difficulty,
                    "Location": row.Location,
                    "Length": row.Length,
                    "Elevation_gain": row.Elevation_gain,
                    "Route_type": row.Route_type,
                    "OwnerID": row.OwnerID,
                    "CreatedAt": str(row.CreatedAt)
                })
            return jsonify(trails)
        except Exception as e:
            logging.error(f"Error fetching trails: {e}")
            abort(500)

    def post(self):
        """Allows admin to create a new trail."""
        """
        ---
        tags:
          - Trails
        summary: Create a new trail
        parameters:
          - name: Authorization
            in: header
            required: true
            type: string
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                Trail_name:
                  type: string
                Trail_Summary:
                  type: string
                Trail_Description:
                  type: string
                Difficulty:
                  type: string
                Location:
                  type: string
                Length:
                  type: number
                Elevation_gain:
                  type: number
                Route_type:
                  type: string
                OwnerID:
                  type: integer
        responses:
          200:
            description: Trail created successfully
          403:
            description: Unauthorized access
          400:
            description: Missing required fields
        """
        # Extract Authorization Header and validate the token
        auth_header = request.headers.get("Authorization")
        decoded_token = validate_token(auth_header)

        # Ensure user has admin privileges
        if decoded_token["role"].lower() != "admin":
            abort(403, description="Unauthorized access: Admin privileges required.")

        # Parse and validate request data
        data = request.json
        try:
            required_fields = [
                "Trail_name", "Trail_Summary", "Trail_Description", "Difficulty",
                "Location", "Length", "Elevation_gain", "Route_type", "OwnerID"
            ]
            for field in required_fields:
                if field not in data:
                    return make_response(jsonify(f"Missing required field: {field}"), 400)

            # Create trail
            result = create_trail(
                conn,
                data["Trail_name"],
                data["Trail_Summary"],
                data["Trail_Description"],
                data["Difficulty"],
                data["Location"],
                data["Length"],
                data["Elevation_gain"],
                data["Route_type"],
                data["OwnerID"]
            )
            return make_response(jsonify({"message": "Trail created successfully"}), 201)
        except Exception as e:
            logging.error(f"Error creating trail: {e}")
            return jsonify({"error": str(e)}), 500


class TrailDetail(Resource):
    def get(self, trail_id):
        """Fetches a specific trail by ID."""
        """
        ---
        tags:
          - Trails
        summary: Get a trail by ID
        parameters:
          - name: trail_id
            in: path
            required: true
            type: integer
        responses:
          200:
            description: Trail details
          404:
            description: Trail not found
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CW2.trails WHERE TrailID = ?", (trail_id,))
            row = cursor.fetchone()
            if row:
                trail = {
                    "TrailID": row.TrailID,
                    "Trail_name": row.Trail_name,
                    "Trail_Summary": row.Trail_Summary,
                    "Trail_Description": row.Trail_Description,
                    "Difficulty": row.Difficulty,
                    "Location": row.Location,
                    "Length": row.Length,
                    "Elevation_gain": row.Elevation_gain,
                    "Route_type": row.Route_type,
                    "OwnerID": row.OwnerID,
                    "CreatedAt": str(row.CreatedAt)
                }
                return jsonify(trail)
            return make_response(jsonify({"error":"Trail not found"}), 404)
        except Exception as e:
            logging.error(f"Error fetching trail: {e}")
            return make_response(jsonify({"error": "Internal Server error"}), 500)

    def put(self, trail_id):
        """Allows admin to update a trail by ID."""
        """
        ---
        tags:
          - Trails
        summary: Update a trail by ID
        parameters:
          - name: Authorization
            in: header
            required: true
            type: string
          - name: trail_id
            in: path
            required: true
            type: integer
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                Trail_name:
                  type: string
                Trail_Summary:
                  type: string
                Trail_Description:
                  type: string
                Difficulty:
                  type: string
                Location:
                  type: string
                Length:
                  type: number
                Elevation_gain:
                  type: number
                Route_type:
                  type: string
        responses:
          200:
            description: Trail updated successfully
          403:
            description: Unauthorized access
          404:
            description: Trail not found
        """
        auth_header = request.headers.get("Authorization")
        decoded_token = validate_token(auth_header)

        if decoded_token["role"].lower() != "admin":
            abort(403, description="Unauthorized access: Admin privileges required.")

        data = request.json
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CW2.trails WHERE TrailID = ?", (trail_id,))
            if cursor.fetchone() is None:
                return make_response(jsonify({"error": "Trail not found"}), 404)

            update_trail(
                conn,
                trail_id,
                trail_name=data.get("Trail_name"),
                trail_summary=data.get("Trail_Summary"),
                trail_description=data.get("Trail_Description"),
                difficulty=data.get("Difficulty"),
                location=data.get("Location"),
                length=data.get("Length"),
                elevation_gain=data.get("Elevation_gain"),
                route_type=data.get("Route_type"),
                owner_id=decoded_token["user_id"]
            )
            return jsonify({"message": "Trail updated successfully!"})
        except Exception as e:
            logging.error(f"Error updating trail: {e}")
            abort(500)

    def delete(self, trail_id):
        """Allows admin to delete a trail by ID."""
        """
        ---
        tags:
          - Trails
        summary: Delete a trail by ID
        parameters:
          - name: Authorization
            in: header
            required: true
            type: string
          - name: trail_id
            in: path
            required: true
            type: integer
        responses:
          200:
            description: Trail deleted successfully
          403:
            description: Unauthorized access
          404:
            description: Trail not found
        """
        auth_header = request.headers.get("Authorization")
        decoded_token = validate_token(auth_header)

        if decoded_token["role"].lower() != "admin":
            abort(403, description="Unauthorized access: Admin privileges required.")

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CW2.trails WHERE TrailID = ?", (trail_id,))
            if cursor.fetchone() is None:
                return make_response(jsonify({"error": "Trail not found"}), 404)

            delete_trail(conn, trail_id)
            return jsonify({"message": "Trail deleted successfully!"})
        except Exception as e:
            logging.error(f"Error deleting trail: {e}")
            abort(500)

# Register resources
api.add_resource(TrailList, "/trails")
api.add_resource(TrailDetail, "/trails/<int:trail_id>")

if __name__ == "__main__":
    print("Swagger UI available at: http://127.0.0.1:5000/apidocs")
    app.run(host="0.0.0.0", port=5000, debug=True)

