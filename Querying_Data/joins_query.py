import sqlalchemy

encoded_password = "Cientra%40123"

url = f"mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/online_shoping?autocommit=True"

engine = sqlalchemy.create_engine(url)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata, autoload_with=engine)
gold_users = sqlalchemy.Table("gold_users", metadata, autoload_with=engine)

with engine.connect() as conn:
    res = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city).where(users.c.user_id.in_(sqlalchemy.select(gold_users.c.uid)))).fetchall()
    for i in res:
        print(i)
    print("\n\n\n\n****************************")
    #-------------------------------FETCH DATA FROM TEO TABLES-----------------------------
    mul_table_quert = conn.execute(sqlalchemy.select(users, gold_users).where(users.c.user_id == gold_users.c.uid)).fetchall()
    for i in mul_table_quert:
        print(i)
    print("\n\n\n\n****************************")
    #-------------------------------FETCH SPECIFIC DATA FROM TEO TABLES-----------------------------
    mul_table_quert = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, gold_users.c.uid, gold_users.c.end_date).where(users.c.user_id == gold_users.c.uid)).fetchall()
    for i in mul_table_quert:
        print(i)

