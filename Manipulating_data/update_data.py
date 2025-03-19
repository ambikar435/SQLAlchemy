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

#stmt = users.update().where(users.c.user_id == 3).values(first_name = "Charan kumar") # cloumn should be valid or else it will throw an CompileError
# we can also use the below stataement
#stmt = users.update().values(phone = "1234512345").where(users.c.user_id == 3)

# if you want to update all the phone numbers with same number use the below command
# users.update().values(phone="6789067890")
#conn.execute(stmt)


select_query = sqlalchemy.select(users)
res_q = conn.execute(select_query).fetchall()
print(res_q)
#Define the ALTER TABLE command to drop columns
#drop_cloumn = conn.execute(sqlalchemy.text("ALTER TABLE users DROP COLUMN last_name;"))
#Define the ALTER TABLE command to add columns
#alter_table_query = """ALTER TABLE users ADD COLUMN phone VARCHAR(15), ADD COLUMN first_name VARCHAR(50), ADD COLUMN last_name VARCHAR(50), ADD COLUMN email_id VARCHAR(100);"""
#conn.execute(sqlalchemy.text(alter_table_query))

describe_persons = conn.execute(sqlalchemy.text("describe users;")).fetchall()
print("Table structure for 'users':")
for row in describe_persons:
    print(row)