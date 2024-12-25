from database_connection import get_db_connection
from crud_operations import create_trail, read_trail, update_trail, delete_trail

if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("Database connected. Running CRUD operations...")

        try:
            # Step 1: Create a new trail
            print("\nCreating a New Trail:")
            create_trail(
                conn,
                'Python Test Trail',
                'Python Summary',
                'Python Description',
                'Moderate',
                'Test Location',
                4.5,
                150,
                'Loop',
                1
            )

            # Step 2: Fetch the TrailID of the newly created trail
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(TrailID) FROM CW2.trails WHERE Trail_name = 'Python Test Trail'")
            new_trail_id = cursor.fetchone()[0]
            print(f"New Trail ID: {new_trail_id}")

            # Step 3: Read trails
            print("\nReading Trails:")
            read_trail(conn)

            # Step 4: Update the newly created trail
            print("\nUpdating Trail:")
            update_trail(conn, new_trail_id, trail_name='Updated Python Trail')

            # Step 5: Delete the newly created trail
            print("\nDeleting Trail:")
            delete_trail(conn, new_trail_id)

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the database connection
            conn.close()
            print("Database connection closed.")
