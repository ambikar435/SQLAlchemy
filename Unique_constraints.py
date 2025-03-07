import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, text, select
from sqlalchemy import UniqueConstraint

print(sqlalchemy.__version__)

user_id = "root"
password = "Cientra@1"
host = "127.0.0.1:3306"
encoded_password = "Cientra%40123"
database_name = "online_shoping"
url_server = f"mysql+pymysql://{user_id}:{encoded_password}@{host}?autocommit=true"

# Step 1: Create the database if it doesn't exist
engine = create_engine(url_server)
with engine.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name};"))

# Step 2: Now that the database is created, create a new connection with the target database
url_with_db = f"mysql+pymysql://{user_id}:{encoded_password}@{host}/{database_name}?autocommit=true"
engine_with_db = create_engine(url_with_db)

metadata = MetaData()

# Define the users table
users = Table("users", metadata, 
              Column('user_id', Integer, nullable=False),
              Column('first_name', String(255), nullable=False),
              Column('last_name', String(255)),
              Column('email_id', String(255)),
              Column('city', String(255)),
              Column('phone', String(255), nullable=False),
              UniqueConstraint('user_id')
)

# Create the table in the database
with engine_with_db.connect() as connection:
    metadata.create_all(engine_with_db)

    # Describe the table
    dsb_cmd = connection.execute(text("DESCRIBE users;")).fetchall()
    print(dsb_cmd)

    # Truncate the table
    connection.execute(text('TRUNCATE TABLE users;'))

    # Insert data into the users table
    connection.execute(users.insert(), [
        {'user_id': 1, 'first_name': "Ambika", 'last_name': "R", 'email_id': "ambika@gmail.com", 'city': "Bangalore", 'phone': "1234567890"},
        {'user_id': 2, 'first_name': "Ashki", 'last_name': "AR", 'email_id': "ashki@gmail.com", 'city': "Bangalore", 'phone': "5432167890"},
        {'user_id': 3, 'first_name': "Charan", 'last_name': "LR", 'email_id': "charan@gmail.com", 'city': "Kolar", 'phone': "0987654321"},
        {'user_id': 4, 'first_name': "Chandu", 'last_name': "LR", 'email_id': "chandu@gmail.com", 'city': "Mangalore", 'phone': "67890123456"}
    ])
    """
    unique_id_error = {'user_id': 4, 'first_name': "Chandu", 'last_name': "LR", 'email_id': "chandu@gmail.com", 'city': "Mangalore", 'phone': "67890123456"}
    connection.execute(users.insert().values(unique_id_error)) # this will raise the unique constrain erroe because user_id 4 is already inserted
    #output= (1062, "Duplicate entry '4' for key 'users.user_id'")

    null_value_error = {'user_id': 5, 'first_name': "Chandu", 'last_name': "LR", 'email_id': "chandu@gmail.com", 'city': "Mangalore", 'phone': None}
    connection.execute(users.insert().values(null_value_error)) # this will raise the value error because we are not passing value for nonnull keys
    # out_put = (1048, "Column 'phone' cannot be null")
    """
    # Select all data from the users table
    select_query = select(users)
    res = connection.execute(select_query).fetchall()

    print(res)
