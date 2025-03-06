import sqlalchemy
from sqlalchemy import MetaData, Table, create_engine, text, Column, Integer, String

user = "root"
password = "Cientra@123"
host_port = "127.0.0.1:3306"  # Make sure the port is correct (3306 for MySQL)
database_name = "first_database"

# URL-encoded password
encoded_password = "Cientra%40123"

engine = create_engine(f'mysql+pymysql://{user}:{encoded_password}@{host_port}/{database_name}')

metadata = MetaData()

Persons = Table('persons', metadata, Column('user_id', Integer), Column('First_name', String(225)), Column("last_name", String(225)), Column("email_id", String(225)), Column("city", String(225)), Column('Phone', String(225)))

with engine.connect() as connection:
    metadata.create_all(engine)
    tables_details = connection.execute(text("show tables;")).fetchall()
    print(tables_details)
    describe_persons = connection.execute(text("describe persons;")).fetchall()
    print(describe_persons)
print("The data base creation is done")
