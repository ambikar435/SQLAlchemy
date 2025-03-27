import sqlalchemy
from datetime import date
encoded_password = "Cientra%40123"

url = f"mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/online_shoping?autocommit=True"

engine = sqlalchemy.create_engine(url)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata, autoload_with=engine)
gold_users = sqlalchemy.Table("gold_users", metadata, autoload_with=engine)

with engine.connect() as conn:
    res = conn.execute(sqlalchemy.select(gold_users).where(gold_users.c.points > 150)).fetchall() # we can use greater then, lessthen, greater then or equal to, less then or equal to 
    print(res)
    opr_and = conn.execute(sqlalchemy.select(gold_users).where(sqlalchemy.sql.and_(gold_users.c.points >= 1000, gold_users.c.points < 2000))).fetchall()
    print(opr_and)
    #**************************************BETWEEN FUNCTION********************************
    #btw_fun = conn.execute(sqlalchemy.select(gold_users).where(gold_users.c.points.between(500,1000))).fetchall() #or
    btw_fun = conn.execute(sqlalchemy.select(gold_users).where(sqlalchemy.between(gold_users.c.points, 200, 700))).fetchall()
    print(btw_fun)
    check_date = conn.execute(sqlalchemy.select(gold_users).where(sqlalchemy.between(gold_users.c.end_date, "2024-05-5", "2025-11-5"))).fetchall()
    print("\n\n\n****")
    print(check_date)