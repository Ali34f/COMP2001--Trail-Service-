from database_connection import get_db_connection
from crud_operations import create_trail, read_trail, update_trail, delete_trail
from authenticator import authenticate_user
import jwt
import datetime

# Secret key for JWT token generation
SECRET_KEY = "your_secret_key"

def generate_token(user_id, role):
    """Generates a JWT token for a user."""
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def validate_token(token):
    """Validates the JWT token."""
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        print("Token has expired. Please log in again.")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token. Please log in again.")
        return None


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

    # Generate a JWT token for the session
    token = generate_token(user_id, user_role)
    print(f"\nLogin successful! JWT Token: {token.decode('utf-8')}")

    conn = get_db_connection()
    if not conn:
        print("Failed to connect to the database. Exiting...")
        return

    print("Database connected. Running CRUD operations...\n")

    try:
        if user_role == 'admin':
            print("\nAdmin operations available. Choose an option:")
            print("1. Create a new trail")
            print("2. Read all trails")
            print("3. Update a trail")
            print("4. Delete a trail")
            print("5. Exit")

            while True:
                choice = input("\nEnter your choice (1-5): ")
                if choice == '1':
                    print("\nCreating a New Trail:")
                    trail_name = input("Trail Name: ")
                    trail_summary = input("Trail Summary: ")
                    trail_description = input("Trail Description: ")
                    difficulty = input("Difficulty: ")
                    location = input("Location: ")
                    length = float(input("Length (km): "))
                    elevation_gain = float(input("Elevation Gain (m): "))
                    route_type = input("Route Type (e.g., Loop, Out-and-back): ")

                    result = create_trail(
                        conn,
                        trail_name,
                        trail_summary,
                        trail_description,
                        difficulty,
                        location,
                        length,
                        elevation_gain,
                        route_type,
                        user_id
                    )
                    print(result.get("message"))

                elif choice == '2':
                    print("\nReading Trails:")
                    trails = read_trail(conn)
                    if trails["status"] == "success":
                        for trail in trails["data"]:
                            print(trail)
                    else:
                        print(trails["message"])

                elif choice == '3':
                    print("\nUpdating a Trail:")
                    trail_id = int(input("Trail ID to update: "))
                    new_name = input("New Trail Name (leave blank to skip): ")
                    new_summary = input("New Trail Summary (leave blank to skip): ")

                    result = update_trail(conn, trail_id, trail_name=new_name, trail_summary=new_summary)
                    print(result.get("message"))

                elif choice == '4':
                    print("\nDeleting a Trail:")
                    trail_id = int(input("Trail ID to delete: "))
                    result = delete_trail(conn, trail_id)
                    print(result.get("message"))

                elif choice == '5':
                    print("Exiting admin operations.")
                    break

                else:
                    print("Invalid choice. Please select from the options.")

        elif user_role == 'user':
            print("\nUser operations available. You can view trails.")
            trails = read_trail(conn)
            if trails["status"] == "success":
                for trail in trails["data"]:
                    print(trail)
            else:
                print(trails["message"])

        else:
            print(f"Role '{user_role}' is not permitted to perform operations.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
