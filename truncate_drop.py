import sqlalchemy
from sqlalchemy import create_engine, select, MetaData, Table, text

user = "root"
password = "Cientra@123"
host_port = "127.0.0.1:3306"  # Make sure the port is correct (3306 for MySQL)
database_name = "first_database"

# URL-encoded password 
encoded_password = "Cientra%40123"

engine = create_engine(f"mysql+pymysql://{user}:{encoded_password}@{host_port}/{database_name}")

metadata = MetaData()
with engine.connect() as connections:
    persons = Table('persons', metadata, autoload_with=engine)
    select_query = select(persons)
    select_res = connections.execute(select_query).fetchall()
    print("Current data in the 'persons' table:")
    for row in select_res:
       print(row)
    connections.execute(text("truncate table persons;"))
    connections.execute(text("drop table persons;"))
    res = connections.execute(text("show tables;")).fetchall()
    #select_res = connections.execute(select_query).fetchall()
    #print(select_res)
    connections.commit()
    print(res)
