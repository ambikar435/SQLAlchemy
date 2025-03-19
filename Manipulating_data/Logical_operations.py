import sqlalchemy
encoded_password = "Cientra%40123"

url = f"mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/online_shoping?autocommit=True"

engine = sqlalchemy.create_engine(url)
metadata = sqlalchemy.MetaData()

with engine.connect() as conn:
    res = conn.execute(sqlalchemy.text("show tables;")).fetchall()
    print(res)

    users = sqlalchemy.Table("users", metadata, autoload_with=engine)
    conduition_and_or = sqlalchemy.sql.and_(users.c.first_name == 'Bob', sqlalchemy.sql.or_(users.c.last_name == "Taylor", users.c.city == "Frankfurt"))
    select_query_and_or = conn.execute(sqlalchemy.select(users).where(conduition_and_or)).fetchall()
    for i in select_query_and_or:
        print(i)
    # USING LIKE METHOD
    print("\n\n\n\nUSING LIKE METHOD")
    select_query_like = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, users.c.email_id).where(users.c.email_id.like("a%"))).fetchall()
    print(select_query_like)
    # USING NOT_LIKE METHOD
    print("\n\n\n\nUSING IN USING NOT_LIKE METHOD")
    select_query_not_like = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, users.c.email_id).where(users.c.email_id.notlike("%yahoo.com"))).fetchall()
    for i in select_query_not_like:
        print(i)

    #USING IN METHOD
    print("\n\n\n\nUSING IN METHOD")
    select_query_IN = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, users.c.email_id).where(users.c.city.in_(["Munich","Leipzig","Cologne"]))).fetchall()
    for i in select_query_IN:
        print(i)

    #USING NOT_IN METHOD
    print("\n\n\n\nUSING NOT_IN METHOD")
    select_query_NOTIN = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.city, users.c.email_id).where(users.c.city.notin_(["Munich","Leipzig","Cologne", "Dusseldorf"]))).fetchall()
    for i in select_query_NOTIN:
        print(i)

    

