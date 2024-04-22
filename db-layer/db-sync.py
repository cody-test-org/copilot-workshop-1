import psycopg2

# Define the connection parameters
db_params = {
    "host": "localhost",
    "database": "mydatabase",
    "user": "postgres",
    "password": "postgres"
}

# Establish a connection to the database
conn = psycopg2.connect(**db_params)

# Create a cursor object
cur = conn.cursor()

# Prepare the SQL query
query = """
    SELECT setval(pg_get_serial_sequence('cats', 'id'), coalesce(max(id),0) + 1, false) FROM cats;
"""