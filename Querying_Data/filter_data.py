import sqlalchemy

encoded_password = "Cientra%40123"

url = f"mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/online_shoping?autocommit=True"

engine = sqlalchemy.create_engine(url)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata, autoload_with=engine)
gold_users = sqlalchemy.Table("gold_users", metadata, autoload_with=engine)

with engine.connect() as conn:
    res = conn.execute(sqlalchemy.text("SELECT CURDATE();")).fetchall()
    print(res)
    exp_date = conn.execute(sqlalchemy.select(gold_users).where(gold_users.c.end_date < sqlalchemy.func.current_date())).fetchall()
    for i in exp_date:
        print("exp date",i)
    active_users = conn.execute(sqlalchemy.select(gold_users).where(gold_users.c.end_date > sqlalchemy.func.current_date())).fetchall()
    for i in active_users:
        print("active users",i)

    #***************************************************************************************************
    #------------------------------ORDERBY METHOD--------------------------------
    print("\n\n\n\n\n*******************************")
    ordr_by = conn.execute(sqlalchemy.select(gold_users).order_by(gold_users.c.points, gold_users.c.uid.desc())).fetchall()
    for i in ordr_by:
        print(i)
    print("###############################################################")
    #------------------------------ORDERBY METHOD --(desc)/(asc)--------------------------------
    print("\n\n\n\n\n*******************************")
    #ordr_by = conn.execute(sqlalchemy.select(gold_users).order_by(gold_users.c.points.desc())).fetchall() 
    ordr_by = conn.execute(sqlalchemy.select(gold_users).order_by(gold_users.c.points.asc())).fetchall() 
    for i in ordr_by:
        print(i)

    #------------------------------LIMIT METHOD --(we can limit the number of records to be fetch))--------------------------------
    print("\n\n\n\n\n*******************************")
    #ordr_by = conn.execute(sqlalchemy.select(gold_users).order_by(gold_users.c.points.desc())).fetchall() 
    ordr_by = conn.execute(sqlalchemy.select(gold_users).order_by(gold_users.c.uid).limit(10)).fetchall() 
    for i in ordr_by:
        print(i)

    #------------------------------OFFSET METHOD ----(ex: offset(20), if we pass number more then the cout of rows this will just print empty list)------------------------------
    print("\n\n\n\n\n*******************************")
    #ordr_by = conn.execute(sqlalchemy.select(gold_users).order_by(gold_users.c.points.desc())).fetchall() 
    ordr_by = conn.execute(sqlalchemy.select(gold_users).order_by(gold_users.c.uid).offset(4)).fetchall()  # offset(4) this will fetch the rows excluding the first 4 rows)
    for i in ordr_by:
        print(i)

