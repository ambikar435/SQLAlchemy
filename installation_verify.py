import sqlalchemy
from sqlalchemy import create_engine, text

user = "root"
password = "Cientra@123"
host_port = "127.0.0.1:3306"  # Make sure the port is correct (3306 for MySQL)
database_name = "first_database"

# URL-encoded password
encoded_password = "Cientra%40123"

# Create the engine and connect
engine = create_engine(f'mysql+pymysql://{user}:{encoded_password}@{host_port}/{database_name}')
with engine.connect() as connection:
    # Wrap the raw SQL statement in text() to make it executable
    connection.execute(text("CREATE DATABASE IF NOT EXISTS first_database"))

    res = connection.execute(text("show databases;")).fetchall()
    glb_vrbl = connection.execute(text("show global variables;")).fetchall()
    glb_vrbl_port = connection.execute(text("show global variables like 'port';")).fetchall()
    tlb_detils = connection.execute(text("show tables;")).fetchall()

    print(res)
    print(glb_vrbl_port)
    print("Tables List:", tlb_detils)

print("Database created successfully or already exists.")
