import pyodbc

def get_db_connection():
    """
    Establishes and returns a connection to the SQL Server database.

    Returns:
        pyodbc.Connection: A connection object if successful, None otherwise.
    """
    try:
        # Connection string to connect to the database
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=dist-6-505.uopnet.plymouth.ac.uk;'
            'DATABASE=COMP2001_JKhan;'
            'UID=JKhan;'
            'PWD=PlymLogin020;'
        )
        return conn
    except pyodbc.Error as e:
        print("Error connecting to the database:", e)
        return None

# Test the connection
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("Connection successful!")
        try:
            # Testing the connection with a sample query
            cursor = conn.cursor()
            cursor.execute("SELECT TOP 5 * FROM CW2.trails")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("Error executing the query:", e)
        finally:
            # Close the connection
            conn.close()
