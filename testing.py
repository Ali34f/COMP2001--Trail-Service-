from database_connection import get_db_connection
from crud_operations import create_trail

conn = get_db_connection()
if conn:
    try:
        create_trail(
            conn,
            "Test Trail",
            "This is a test summary",
            "This is a test description",
            "Easy",
            "Test Location",
            5.5,
            200,
            "Loop",
            1
        )
        print("Trail created successfully!")
    except Exception as e:
        print(f"Error creating trail: {e}")
