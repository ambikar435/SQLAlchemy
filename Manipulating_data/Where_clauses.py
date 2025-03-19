import sqlalchemy

user_id = "root"
password = "Cientra@1"
host = "127.0.0.1:3306"
encoded_password = "Cientra%40123"
database_name = "online_shoping"
url_server = f"mysql+pymysql://{user_id}:{encoded_password}@{host}/{database_name}?autocommit=true"

engine = sqlalchemy.create_engine(url_server)
conn = engine.connect()

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table('users', metadata, autoload_with=engine)

select_query = sqlalchemy.select(users)
res = conn.execute(select_query).fetchall()


select_query_with_where = sqlalchemy.select(users).where(users.c.city == "Kolar")
res = conn.execute(select_query_with_where).fetchall()

print(res)
print("\n\n\n")
print(users.c) #returns the cloumn names 
#result is : [ReadOnlyColumnCollection(users.user_id, users.first_name, users.last_name, users.email_id, users.city, users.phone)]

select_specific_code = sqlalchemy.select(users.c.user_id, users.c.phone, users.c.city).where(users.c.city == "Bangalore") # selelt the sepcfic column 
res1 = conn.execute(select_specific_code).fetchall()
print("\n\n\n")
print(res1)
