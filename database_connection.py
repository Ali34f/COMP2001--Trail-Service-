import pyodbc

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=dist-6-505.uopnet.plymouth.ac.uk;'
            'DATABASE=COMP2001_JKhan;'
            'UID=JKhan;'
            'PWD=PlymLogin020;'
        )
        print("Database connection successful!")
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT TOP 5 * FROM CW2.trails")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()
