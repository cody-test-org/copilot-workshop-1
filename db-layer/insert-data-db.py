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
    INSERT INTO cats (id, name, age, breed)
    VALUES (%s, %s, %s, %s)
"""
data = (12, 'Chairman Meow', 3, 'Siamese')  # Replace with your actual data

# Execute the SQL query
cur.execute(query, data)

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()