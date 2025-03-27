#fetchone() gives you the the row of values enclosed in tuple
#fetchall() gives you all the rows in the table
#fetchmany(6) gives the total number of rows based on user input

import sqlalchemy

encoded_password = "Cientra%40123"

url = f"mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/online_shoping?autocommit=True"

engine = sqlalchemy.create_engine(url)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata, autoload_with=engine)
gold_users = sqlalchemy.Table("gold_users", metadata, autoload_with=engine)

with engine.connect() as conn:
    #-----------------------------------FETCHALL()------------------------------------------------------
    fetch_all = conn.execute(sqlalchemy.select(gold_users).where(sqlalchemy.sql.and_(gold_users.c.points >= 100, gold_users.c.points < 2000))).fetchall()
    print(fetch_all)
    print("\n\n\n\n**************************")
    #-----------------------------------FETCHONE()------------------------------------------------------
    fetch_one = conn.execute(sqlalchemy.select(gold_users).where(sqlalchemy.sql.and_(gold_users.c.points >= 1000, gold_users.c.points < 2000))).fetchone()
    print(fetch_one)
    print("\n\n\n\n**************************")
    #-----------------------------------FETCHMANY()------------------------------------------------------
    fetch_many = conn.execute(sqlalchemy.select(gold_users).where(sqlalchemy.sql.and_(gold_users.c.points >= 1000, gold_users.c.points < 2000))).fetchmany(2)
    print(fetch_many)