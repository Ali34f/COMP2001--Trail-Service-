import pyodbc

try:
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=dist-6-505.uopnet.plymouth.ac.uk;"
        "DATABASE=COMP2001_JKhan;"
        "UID=JKhan;"
        "PWD=PLymLogin020;"
    )
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
