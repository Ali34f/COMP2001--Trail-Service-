from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
from flasgger import Swagger
from database_connection import get_db_connection
from crud_operations import create_trail, read_trail, update_trail, delete_trail
from authenticator import authenticate_user
import logging

app = Flask(__name__)
api = Api(app)
Swagger(app)

logging.basicConfig(level=logging.DEBUG)

# Database connection
conn = get_db_connection()
if conn is None:
    raise ConnectionError("Database connection failed. Check your database settings.")

# Global variable to simulate a session
current_user = None

def log_error(e):
    """Logs an error and returns a JSON error response."""
    logging.error(f"An error occurred: {e}")
    return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    """Serves the index.html for the front-end."""
    return render_template("index.html")

@app.route("/auth", methods=["POST"])
def login():
    """Handles user login and sets the current_user session."""
    global current_user
    data = request.json
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"error": "Email and password are required."}), 400

    user = authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Authentication failed."}), 401

    current_user = user
    return jsonify({"message": "Login successful!", "role": user["role"], "user_id": user["user_id"]})

# Resource: Trails
class TrailList(Resource):
    def get(self):
        """Fetches all trails."""
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
            return log_error(e)

    def post(self):
        """Allows admin to create a new trail."""
        if current_user is None or current_user["role"].lower() != "admin":
            return jsonify({"error": "Unauthorized access"}), 403

        data = request.json
        try:
            # Validate required fields
            required_fields = [
                "Trail_name", "Trail_Summary", "Trail_Description", "Difficulty",
                "Location", "Length", "Elevation_gain", "Route_type", "OwnerID"
            ]
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Missing required field: {field}"}), 400

            # Validate field types
            if not isinstance(data["Trail_name"], str) or len(data["Trail_name"].strip()) == 0:
                return jsonify({"error": "Trail_name must be a non-empty string"}), 400
            if not isinstance(data["Length"], (int, float)) or data["Length"] <= 0:
                return jsonify({"error": "Length must be a positive number"}), 400
            if not isinstance(data["Elevation_gain"], (int, float)) or data["Elevation_gain"] < 0:
                return jsonify({"error": "Elevation_gain must be a non-negative number"}), 400

            # Attempt to create the trail
            create_trail(
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

            # Return success response
            return jsonify({"message": "Trail created successfully!"}), 201

        except Exception as e:
            logging.error(f"Error creating trail: {e}")
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500


class TrailDetail(Resource):
    def get(self, trail_id):
        """Fetches a specific trail by ID."""
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
            return jsonify({"message": "Trail not found"}), 404
        except Exception as e:
            return log_error(e)

    def delete(self, trail_id):
        """Allows admin to delete a trail by ID."""
        if current_user is None or current_user["role"].lower() != "admin":
            return jsonify({"error": "Unauthorized access"}), 403

        try:
            delete_trail(conn, trail_id)
            return jsonify({"message": "Trail deleted successfully!"})
        except Exception as e:
            return log_error(e)

    def put(self, trail_id):
        """Allows admin to update a trail by ID."""
        if current_user is None or current_user["role"].lower() != "admin":
            return jsonify({"error": "Unauthorized access"}), 403

        data = request.json
        try:
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
                owner_id=current_user["user_id"]
            )
            return jsonify({"message": "Trail updated successfully!"})
        except Exception as e:
            return log_error(e)

# Register resources
api.add_resource(TrailList, "/trails")
api.add_resource(TrailDetail, "/trails/<int:trail_id>")

if __name__ == "__main__":
    app.run(debug=True)
