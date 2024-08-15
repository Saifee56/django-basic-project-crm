import psycopg2
from psycopg2 import sql

# Database connection parameters
db_name = "saifee"
user = "postgres"
password = "1234"
host = "localhost"
port = "5432"

# Connect to the default 'postgres' database
conn = psycopg2.connect(
    dbname="postgres",
    user=user,
    password=password,
    host=host,
    port=port
)
conn.autocommit = True

# Create a new cursor
cur = conn.cursor()

# SQL command to create a new database
create_db_query = sql.SQL("CREATE DATABASE {}").format(
    sql.Identifier(db_name)
)

# Execute the SQL command
try:
    cur.execute(create_db_query)
    print(f"Database '{db_name}' created successfully.")
except Exception as e:
    print(f"Error: {e}")

# Close the cursor and connection
cur.close()
conn.close()
