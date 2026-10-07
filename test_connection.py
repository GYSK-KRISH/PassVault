import os
import mysql.connector

def test_db():
    print("=" * 50)
    print(" PassVault Database Connection Tester")
    print("=" * 50)

    host = os.getenv("PASSVAULT_DB_HOST", "localhost")
    user = os.getenv("PASSVAULT_DB_USER", "root")
    password = os.getenv("PASSVAULT_DB_PASSWORD", "")
    database = os.getenv("PASSVAULT_DB_NAME", "passvault_db")

    if not password:
        password = input("Enter your local MySQL password: ").strip()

    print(f"\nAttempting connection to MySQL server at '{host}' as user '{user}'...")

    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(" SUCCESS! Connected to database 'passvault_db'.")
        
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = [t[0] for t in cursor.fetchall()]
        print(f" Tables found: {tables}")
        
        if "credentials" in tables:
            print(" 'credentials' table is present and ready!")
        else:
            print(" WARNING: 'credentials' table not found. Please run database.sql in MySQL Workbench.")
            
        cursor.close()
        conn.close()
        
        print("\nNow you can launch the app by setting the password variable:")
        print(f'   $env:PASSVAULT_DB_PASSWORD = "{password}"')
        print('   python app.py')

    except mysql.connector.Error as err:
        print(f"\n CONNECTION FAILED!")
        print(f"Error Details: {err}")
        print("\nTroubleshooting Tips:")
        if err.errno == 1045:
            print(" -> Access Denied: The password or username is incorrect.")
        elif err.errno == 1049:
            print(" -> Unknown Database: Please execute database.sql in MySQL Workbench.")
        elif err.errno == 2003:
            print(" -> Can't connect to MySQL server: Ensure MySQL service is running in Windows Services / MySQL Workbench.")

if __name__ == "__main__":
    test_db()
