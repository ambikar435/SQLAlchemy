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
users = sqlalchemy.Table("users", metadata, autoload_with=engine)


#****************Alter Query*****************************************************

conn.execute(sqlalchemy.text("alter table users modify column email_id varchar(255) unique;"))

des_select_query_1 = conn.execute(sqlalchemy.text("describe users;")).fetchall()
for i in des_select_query_1:
    print(i)

conn.execute(users.insert().values({'user_id': 5, 'first_name': "Chandana", 'last_name': "LR", 'email_id': "chandana@gmail.com", 'city': "Mangalore", 'phone': "67890123456"}))

select_query = sqlalchemy.select(users)
res = conn.execute(select_query).fetchall()
for i in res:
    print(i)

# *******************************Delete Query **************************************

conn.execute(users.delete().where(users.c.user_id == "5")) 

select_query = sqlalchemy.select(users)
res = conn.execute(select_query).fetchall()
for i in res:
    print(i)

""""
"*****************************************************************************************************************************
******************************************************************************************************************************
------------------------------------------UPDATE TABLE------------------------------------------------------------------------
""****************************************************************************************************************************
******************************************************************************************************************************
"""

print("\n\n\n\n\n")


indexes = conn.execute(sqlalchemy.text("SHOW INDEX FROM users;")).fetchall()
index_names = [index[2] for index in indexes] 
# Drop all indexes except 'PRIMARY'
for index in index_names:
    if index != "PRIMARY":  # Ensure we do not drop the primary key
        conn.execute(sqlalchemy.text(f"ALTER TABLE users DROP INDEX {index};")) # Note: here we are droping the index not the column
        # if went to drop cloumn then we want to use DROP COLUMN email_id 
        conn.commit()
        print(f"Dropped index: {index}")

print("✅ All duplicate indexes have been removed.")
print("\n**************\n")


print(conn.execute(sqlalchemy.text("show create table users;")).fetchall())
print("****************")
print("^^^^^^^^^^^^^^^^^^^")

des_select_query = conn.execute(sqlalchemy.text("describe users;")).fetchall()
for i in des_select_query:
    print(i)