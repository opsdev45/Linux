from flask import Flask
import psycopg2  # Import psycopg2 library for database connection

app = Flask(__name__)

# Replace with your database connection details (obtained from PostgreSQL container)
DB_HOST = "postgres"  # Name of the PostgreSQL service in docker-compose
DB_NAME = "mydatabase"
DB_USER = "postgres"
DB_PASSWORD = "password"  # Replace with a strong password

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        return connection
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

@app.route("/")
def hello_world():
    connection = connect_to_db()
    if connection:
        # Simulate a database interaction (replace with your actual logic)
        cursor = connection.cursor()
        cursor.execute("SELECT 1 + 1;")
        result = cursor.fetchone()[0]
        connection.close()
        return f"Hello, from my Flask app! (Database result: {result})"
    else:
        return "Failed to connect to database."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
