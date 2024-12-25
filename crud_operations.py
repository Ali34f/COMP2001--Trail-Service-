import pyodbc

def create_trail(conn, trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_type, owner_id):
    try:
        cursor = conn.cursor()
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
            @OwnerID = ?""",
            trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_type, owner_id)
        conn.commit()
        print("Trail created successfully!")
    except pyodbc.Error as e:
        print("Error creating trail:", e)

def read_trail(conn, trail_id=None, trail_name=None, owner_id=None):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            EXEC CW2.ReadTrail
            @TrailID = ?, 
            @Trail_name = ?, 
            @OwnerID = ?""",
            trail_id, trail_name, owner_id)
        for row in cursor.fetchall():
            print(row)
    except pyodbc.Error as e:
        print("Error reading trail:", e)

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
            @OwnerID = ?""",
            trail_id, trail_name, trail_summary, trail_description, difficulty, location, length, elevation_gain, route_type, owner_id)
        conn.commit()
        print("Trail updated successfully!")
    except pyodbc.Error as e:
        print("Error updating trail:", e)

def delete_trail(conn, trail_id):
    try:
        cursor = conn.cursor()
        cursor.execute("EXEC CW2.DeleteTrail @TrailID = ?", trail_id)
        conn.commit()
        print("Trail deleted successfully!")
    except pyodbc.Error as e:
        print("Error deleting trail:", e)
