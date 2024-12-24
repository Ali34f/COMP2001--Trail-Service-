import pyodbc

try:
    # Connection string to connect to the database
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=dist-6-505.uopnet.plymouth.ac.uk;'  # Replace with your server
        'DATABASE=YourDatabaseName;'               # Replace with your database
        'UID=YourUsername;'                        # Replace with your username
        'PWD=YourPassword;'                        # Replace with your password
    )

    print("Connection successful!")

    # Testing the connection with a sample query
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 5 * FROM YourTableName")  # Replace with a valid table name
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

except pyodbc.Error as e:
    print("Error:", e)