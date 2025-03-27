#mainly Having clause is used when the group by functions dont support where operation for aggregator operations like (>,<, ==, etc)
# we can use having function istand of where

import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:Cientra%40123@127.0.0.1:3306/online_shoping?autocommit=True")

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata, autoload_with=engine)
gold_users = sqlalchemy.Table("gold_users", metadata, autoload_with=engine)
products = sqlalchemy.Table("products", metadata, autoload_with=engine)

with engine.connect() as conn:
    #---------------------------------------HAVING------------------------------------
    res = conn.execute(sqlalchemy.select(products.c.prod_name, sqlalchemy.func.max(products.c.price)).group_by(products.c.prod_name).having(sqlalchemy.func.max(products.c.price > 200))).fetchall()
    print(res)
    #HAVING is used only with aggregate functions (like MAX(), MIN(), AVG(), COUNT()).
    print("\n\n\n\n---------------------------------------HAVING------------------------------------")
    res = conn.execute(sqlalchemy.select(products.c.prod_name, sqlalchemy.func.min(products.c.price)).group_by(products.c.prod_name).having(sqlalchemy.func.min(products.c.price) < 200)).fetchall()
    print(res)

    print("\n\n\n\n---------------------------------------HAVING--(SELECTING more column data to group)----------------------------------")
    res = conn.execute(sqlalchemy.select(products.c.prod_name, sqlalchemy.func.min(products.c.price), sqlalchemy.func.sum(products.c.price)).group_by(products.c.prod_name).having(sqlalchemy.func.min(products.c.price) < 200)).fetchall()
    print(res)
    #inside -----------HAVING-------------we can use AND, OR, NOT OPERATIONS ALSO-----------------

