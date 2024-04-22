import psycopg2
from prettytable import PrettyTable

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

# Execute a SQL query
cur.execute("SELECT * FROM cats")

# Fetch all rows
rows = cur.fetchall()

# Print the rows
table = PrettyTable(["id", "name", "age", "breed"])  # Replace with your column names
for row in rows:
    table.add_row(row)

print(table)

# Close the cursor and the connection
cur.close()
conn.close()