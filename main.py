from database_connection import get_db_connection
from crud_operations import create_trail, read_trail, update_trail, delete_trail
from authenticator import authenticate_user


def main():
    # Authenticate the user
    print("Please log in:")
    email = input("Email: ")
    password = input("Password: ")

    user = authenticate_user(email, password)
    if not user:
        print("Authentication failed. Exiting...")
        return

    user_role = user.get('role', '').lower()
    user_id = user.get('user_id')

    if not user_role or not user_id:
        print("Invalid user data received. Exiting...")
        return

    conn = get_db_connection()
    if not conn:
        print("Failed to connect to the database. Exiting...")
        return

    print("Database connected. Running CRUD operations...")

    try:
        if user_role == 'admin':
            print("\nAdmin operations available.")

            # Step 1: Create a new trail
            print("\nCreating a New Trail:")
            create_trail(
                conn,
                'Admin Test Trail',
                'Admin Summary',
                'Admin Description',
                'Moderate',
                'Admin Location',
                4.5,
                150,
                'Loop',
                user_id
            )

            # Step 2: Fetch the TrailID of the newly created trail
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(TrailID) FROM CW2.trails WHERE Trail_name = 'Admin Test Trail'")
            new_trail_id = cursor.fetchone()[0]
            print(f"New Trail ID: {new_trail_id}")

            # Step 3: Read trails
            print("\nReading Trails:")
            read_trail(conn)

            # Step 4: Update the newly created trail
            print("\nUpdating Trail:")
            update_trail(conn, new_trail_id, trail_name='Updated Admin Trail')

            # Step 5: Delete the newly created trail
            print("\nDeleting Trail:")
            delete_trail(conn, new_trail_id)

        elif user_role == 'user':
            print("\nUser operations available. You can view trails.")

            # Read trails
            print("\nReading Trails:")
            read_trail(conn)

        else:
            print(f"Role '{user_role}' is not permitted to perform operations.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
