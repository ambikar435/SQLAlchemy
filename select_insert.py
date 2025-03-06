import sqlalchemy
from sqlalchemy import MetaData, Table, create_engine, text, Column, Integer, String, select
from sqlalchemy.exc import SQLAlchemyError

user = "root"
password = "Cientra@123"
host_port = "127.0.0.1:3306"  # Make sure the port is correct (3306 for MySQL)
database_name = "first_database"

# URL-encoded password
encoded_password = "Cientra%40123"

# Create the engine and connect
engine = create_engine(f'mysql+pymysql://{user}:{encoded_password}@{host_port}/{database_name}')
metadata = MetaData()

# Define the 'persons' table schema (ensure user_id is the primary key)
persons = Table('persons', metadata,
                Column('user_id', Integer, primary_key=True),
                Column('First_name', String(225)),
                Column('last_name', String(225)),
                Column('email_id', String(225)),
                Column('city', String(225)),
                Column('Phone', String(225)))

try:
    with engine.connect() as connection:
        # Create tables if they don't exist
        metadata.create_all(engine)
        
        # Show the existing tables
        tables_details = connection.execute(text("show tables;")).fetchall()
        print(f"Existing tables: {tables_details}")
        
        # Describe the persons table
        describe_persons = connection.execute(text("describe persons;")).fetchall()
        print("Table structure for 'persons':")
        for row in describe_persons:
            print(row)
        
        # Select query to fetch all records from 'persons' table
        select_query = select(persons)
        select_results = connection.execute(select_query).fetchall()  # Execute the SELECT query
        print("Current records in the 'persons' table:")
        print(select_results)
        
        # Insert individual records
        ins = persons.insert().values(user_id=1, First_name="Ambika", last_name="R", email_id="ambika@gmail.com", city="Nammuru", Phone="1234567890")
        connection.execute(ins)
        
        ins_1 = persons.insert().values(user_id=2, First_name="Chandu", last_name="LR", email_id="chandu2001@gmail.com", city="Bangalore", Phone="0987654321")
        connection.execute(ins_1)
        
        # Insert multiple records in batch
        connection.execute(persons.insert(), [
            {"user_id": 3, "First_name": "Ashki", "last_name": "R", "email_id": "ashki.ash@gmail.com", "city": "Mangalore", "Phone": "2345672345"}
        ])
        
        # Fetch updated results after inserts
        select_results = connection.execute(select_query).fetchall()
        connection.commit()
        print("Updated records in the 'persons' table:")
        print(select_results)

except SQLAlchemyError as e:
    print(f"An error occurred: {e}")
finally:
    print("Database operation complete.")
