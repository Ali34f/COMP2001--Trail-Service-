from database_connection import get_db_connection
from crud_operations import create_trail, read_trail, update_trail, delete_trail

def test_crud_operations():
    # Get database connection
    conn = get_db_connection()

    if conn is None:
        print("Database connection failed.")
        return

    try:
        print("\n--- Testing Create Trail ---")
        create_trail(
            conn,
            trail_name="Test Trail",
            trail_summary="Test Summary",
            trail_description="Test Description",
            difficulty="Moderate",
            location="Test Location",
            length=5.0,
            elevation_gain=100,
            route_type="Loop",
            owner_id=1
        )
        print("Create operation successful.")

        print("\n--- Testing Read Trail ---")
        trails = read_trail(conn)
        print("Read operation successful. Trails fetched:")
        for trail in trails:
            print(trail)

        if trails:
            test_trail_id = trails[-1]["TrailID"]

            print("\n--- Testing Update Trail ---")
            update_trail(
                conn,
                trail_id=test_trail_id,
                trail_name="Updated Test Trail",
                trail_summary="Updated Summary"
            )
            print("Update operation successful.")

            print("\n--- Testing Delete Trail ---")
            delete_trail(conn, trail_id=test_trail_id)
            print("Delete operation successful.")

    except Exception as e:
        print(f"Error during CRUD tests: {e}")
    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    test_crud_operations()
