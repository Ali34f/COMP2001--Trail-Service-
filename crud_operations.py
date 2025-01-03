import pyodbc
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def create_trail(conn, trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_type, owner_id):
    """
    Create a new trail in the database.
    """
    try:
        cursor = conn.cursor()
        logging.debug("Executing CreateTrail procedure...")

        # Execute the stored procedure or SQL query
        cursor.execute("""
            EXEC CW2.CreateTrail
                @Trail_name = ?, 
                @Trail_Summary = ?, 
                @Trail_Description = ?, 
                @Difficulty = ?, 
                @Location = ?, 
                @Length = ?, 
                @Elevation_gain = ?, 
                @Route_type = ?, 
                @OwnerID = ?
        """, trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_type, owner_id)

        # Commit the transaction
        conn.commit()
        logging.debug("Trail created successfully in the database.")

        # Return a success message as a dictionary
        return {"status": "success", "message": "Trail created successfully"}

    except pyodbc.Error as e:
        # Log and raise database errors as JSON-serializable dictionary
        logging.error(f"Database Error: {e}")
        return {"status": "error", "message": f"Database Error: {e}"}

    except Exception as e:
        # Log and raise general errors as JSON-serializable dictionary
        logging.error(f"Error creating trail: {e}")
        return {"status": "error", "message": f"Error creating trail: {e}"}



def read_trail(conn, trail_id=None, trail_name=None, owner_id=None):
    """
    Read trail(s) from the database.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            EXEC CW2.ReadTrail
            @TrailID = ?, 
            @Trail_name = ?, 
            @OwnerID = ?""",
            trail_id, trail_name, owner_id)
        results = cursor.fetchall()
        trails = []
        for row in results:
            trails.append({
                "TrailID": row.TrailID,
                "Trail_name": row.Trail_name,
                "Trail_Summary": row.Trail_Summary,
                "Trail_Description": row.Trail_Description,
                "Difficulty": row.Difficulty,
                "Location": row.Location,
                "Length": float(row.Length),
                "Elevation_gain": float(row.Elevation_gain),
                "Route_type": row.Route_type,
                "OwnerID": row.OwnerID,
                "CreatedAt": str(row.CreatedAt)
            })
        return trails
    except pyodbc.Error as e:
        logging.error(f"Error reading trail: {e}")
        raise Exception(f"Error reading trail: {e}")

def update_trail(conn, trail_id, trail_name=None, trail_summary=None, trail_description=None, difficulty=None, location=None, length=None, elevation_gain=None, route_type=None, owner_id=None):
    """
    Update an existing trail in the database.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            EXEC CW2.UpdateTrail
            @TrailID = ?, 
            @Trail_name = ?, 
            @Trail_Summary = ?, 
            @Trail_Description = ?, 
            @Difficulty = ?, 
            @Location = ?, 
            @Length = ?, 
            @Elevation_gain = ?, 
            @Route_type = ?, 
            @OwnerID = ?""",
            trail_id, trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_type, owner_id)
        conn.commit()
        logging.info("Trail updated successfully!")
    except pyodbc.Error as e:
        logging.error(f"Error updating trail: {e}")
        raise Exception(f"Error updating trail: {e}")

def delete_trail(conn, trail_id):
    """
    Delete a trail from the database.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("EXEC CW2.DeleteTrail @TrailID = ?", trail_id)
        conn.commit()
        logging.info("Trail deleted successfully!")
    except pyodbc.Error as e:
        logging.error(f"Error deleting trail: {e}")
        raise Exception(f"Error deleting trail: {e}")