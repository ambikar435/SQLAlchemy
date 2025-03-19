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

# in sql use "and", "or", Not will raise some conflicts better to use inbuilt sqlalchemy conditional operations

# check "AND"
and_condition = sqlalchemy.sql.and_(users.c.city == "kolar", users.c.last_name == 'LR')

select_and_query = sqlalchemy.select(users).where(and_condition)
and_res = conn.execute(select_and_query).fetchall()
print(and_res)

#Check "OR"
print("\n\n\n\n")
or_condition = sqlalchemy.sql.or_(users.c.city == "Bangalore", users.c.last_name == "LR")
select_or_query = sqlalchemy.select(users).where(or_condition)
or_res = conn.execute(select_or_query).fetchall()
print(or_res)

print("\n\n\n")

#CHECK NOT

not_condtion = sqlalchemy.sql.not_(users.c.city == "Kolar")
select_not_query = sqlalchemy.select(users).where(not_condtion)
not_result = conn.execute(select_not_query).fetchall()
print(not_result)

#****************************LIKE METHOD*********************
print("\n")
print("***************")
print("\n")
select_like_query = sqlalchemy.select(users.c.user_id, users.c.city, users.c.first_name).where(users.c.city.like("%E"))
like_result = conn.execute(select_like_query).fetchall()
print(like_result)

#****************************BETWEEEN METHOD*********************


print("\n")
print("***************")
print("\n")
select_between_query = sqlalchemy.select(users.c.user_id, users.c.city, users.c.first_name).where(users.c.city.between("A", "KP")) 
# users.c.city.between("A", "K") including A EXCLUDING K
# users.c.city.between("A", "Kp") INCLUDING A AND K BUT data will be displayed which starts with K and second characters should be in range of a to p (excluding p) "Kp" 
between_result = conn.execute(select_between_query).fetchall()
print(between_result)

#****************************Text METHOD from sqlalchemy.sql*********************

from sqlalchemy.sql import text

text_query = text("""SELECT first_name, last_name, city FROM users WHERE city = :user_city AND last_name = :user_last_name""")
res_text = conn.execute(text_query, {'user_city' : "Kolar", 'user_last_name' : "LR"}).fetchall()
print(res_text)

