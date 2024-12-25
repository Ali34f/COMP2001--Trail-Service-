from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flasgger import Swagger
from database_connection import get_db_connection
from crud_operations import create_trail, read_trail, update_trail, delete_trail

app = Flask(__name__)
api = Api(app)
Swagger(app)

# Database connection
conn = get_db_connection()

# Resource: Trails
class TrailList(Resource):
    def get(self):
        """Get all trails
        ---
        responses:
          200:
            description: A list of all trails
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
            return jsonify({"error": str(e)}), 500

    def post(self):
        """Create a new trail
        ---
        parameters:
          - name: body
            in: body
            required: true
            description: The trail details
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
          201:
            description: Trail created successfully
        """
        data = request.json
        try:
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
            return jsonify({"message": "Trail created successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


# Resource: TrailDetail
class TrailDetail(Resource):
    def get(self, trail_id):
        """Get trail by ID
        ---
        parameters:
          - name: trail_id
            in: path
            required: true
            type: integer
            description: The trail ID
        responses:
          200:
            description: Trail details
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CW2.trails WHERE TrailID = ?", trail_id)
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
            return jsonify({"error": str(e)}), 500

    def put(self, trail_id):
        """Update a trail
        ---
        parameters:
          - name: trail_id
            in: path
            required: true
            type: integer
            description: The trail ID
          - name: body
            in: body
            required: true
            description: The updated trail details
        responses:
          200:
            description: Trail updated successfully
        """
        data = request.json
        try:
            update_trail(
                conn,
                trail_id,
                data.get("Trail_name"),
                data.get("Trail_Summary"),
                data.get("Trail_Description"),
                data.get("Difficulty"),
                data.get("Location"),
                data.get("Length"),
                data.get("Elevation_gain"),
                data.get("Route_type"),
                data.get("OwnerID")
            )
            return jsonify({"message": "Trail updated successfully!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete(self, trail_id):
        """Delete a trail
        ---
        parameters:
          - name: trail_id
            in: path
            required: true
            type: integer
            description: The trail ID
        responses:
          200:
            description: Trail deleted successfully
        """
        try:
            delete_trail(conn, trail_id)
            return jsonify({"message": "Trail deleted successfully!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500


# Register resources
api.add_resource(TrailList, "/trails")
api.add_resource(TrailDetail, "/trails/<int:trail_id>")

if __name__ == "__main__":
    app.run(debug=True)
