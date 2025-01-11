import pyodbc
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def create_trail(conn, trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_type, owner_id):
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

        conn.commit()
        logging.debug("Trail created successfully in the database.")
        return {"status": "success", "message": "Trail created successfully"}

    except pyodbc.IntegrityError as e:
        logging.error(f"Database Integrity Error: {e}")
        return {"status": "error", "message": "Database integrity error. Check input values.", "error": str(e)}

    except pyodbc.ProgrammingError as e:
        logging.error(f"Database Programming Error: {e}")
        return {"status": "error", "message": "Database programming error. Verify stored procedures.", "error": str(e)}

    except Exception as e:
        logging.error(f"Unexpected error creating trail: {e}")
        return {"status": "error", "message": "Unexpected error occurred.", "error": str(e)}


def read_trail(conn, trail_id=None):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM CW2.trails WHERE TrailID = ?
        """, trail_id)
        row = cursor.fetchone()

        if not row:
            return {"status": "error", "message": f"Trail with ID {trail_id} not found."}

        trail = {
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
        }
        return {"status": "success", "data": trail}

    except pyodbc.Error as e:
        logging.error(f"Error reading trail: {e}")
        return {"status": "error", "message": "Database error while reading trail.", "error": str(e)}

    except Exception as e:
        logging.error(f"Unexpected error reading trail: {e}")
        return {"status": "error", "message": "Unexpected error occurred.", "error": str(e)}


def update_trail(conn, trail_id, trail_name=None, trail_summary=None, trail_description=None, difficulty=None, location=None, length=None, elevation_gain=None, route_type=None, owner_id=None):
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
            @OwnerID = ?
        """, trail_id, trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_type, owner_id)

        rows_affected = cursor.rowcount
        conn.commit()

        if rows_affected == 0:
            return {"status": "error", "message": f"Trail with ID {trail_id} not found."}

        logging.info("Trail updated successfully!")
        return {"status": "success", "message": "Trail updated successfully"}

    except pyodbc.Error as e:
        logging.error(f"Error updating trail: {e}")
        return {"status": "error", "message": "Database error while updating trail.", "error": str(e)}

    except Exception as e:
        logging.error(f"Unexpected error updating trail: {e}")
        return {"status": "error", "message": "Unexpected error occurred.", "error": str(e)}


def delete_trail(conn, trail_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM CW2.trails WHERE TrailID = ?", trail_id)

        rows_affected = cursor.rowcount
        conn.commit()

        if rows_affected == 0:
            return {"status": "error", "message": f"Trail with ID {trail_id} not found."}

        logging.info("Trail deleted successfully!")
        return {"status": "success", "message": f"Trail with ID {trail_id} deleted successfully."}

    except pyodbc.Error as e:
        logging.error(f"Error deleting trail: {e}")
        return {"status": "error", "message": "Database error while deleting trail.", "error": str(e)}

    except Exception as e:
        logging.error(f"Unexpected error deleting trail: {e}")
        return {"status": "error", "message": "Unexpected error occurred.", "error": str(e)}
