#Cross joins match every tuple in one table to every tuple in another table

import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:Cientra%40123@127.0.0.1:3306/online_shoping?autocommit=True")

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table('users', metadata, autoload_with=engine)
gold_users = sqlalchemy.Table('gold_users', metadata, autoload_with=engine)

with engine.connect() as conn:
    # Not recommended to use
    res = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, gold_users.c.uid, users.c.user_id, gold_users.c.end_date, gold_users.c.points)).fetchall()
    for i in res:
        print(i)

    print("\n\n\n\n**************")
    res = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, gold_users.c.uid, users.c.user_id, gold_users.c.end_date, gold_users.c.points).where(sqlalchemy.sql.and_(users.c.user_id == gold_users.c.uid, gold_users.c.end_date > sqlalchemy.func.current_date()))).fetchall()
    for i in res:
        print(i)

    """
    we can also use alias
    c = users.alias() this we can use as c.c.first_name, c.c.last_name etc
    g = gold_users.alias() this can use as g.c.uid etc

    """
    
    #-----------------------------JOINS--(INNER JOIN)----------------------------------------
    res = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, gold_users.c.uid, users.c.user_id, gold_users.c.end_date, gold_users.c.points).select_from(users.join(gold_users, users.c.user_id == gold_users.c.uid))).fetchall()
    print("-----------------------------JOINS--(INNER JOINS)--------------------------------------")
    for i in res:
        print(i)

    #-----------------------------JOINS--(INNER JOIN)----------------------------------------
    res = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, gold_users.c.uid, users.c.user_id, gold_users.c.end_date, gold_users.c.points).select_from(users.outerjoin(gold_users, users.c.user_id == gold_users.c.uid))).fetchall()
    print("-----------------------------JOINS--(OUTER JOINS)--------------------------------------")
    for i in res:
        print(i)