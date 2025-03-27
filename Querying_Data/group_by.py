import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:Cientra%40123@127.0.0.1:3306/online_shoping?autocommit=True")

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata, autoload_with=engine)
gold_users = sqlalchemy.Table("gold_users", metadata, autoload_with=engine)

products = sqlalchemy.Table("products", metadata, sqlalchemy.Column("prod_id", sqlalchemy.Integer, nullable=False, unique=True, primary_key=True, autoincrement=False), sqlalchemy.Column("prod_name", sqlalchemy.String(255)), sqlalchemy.Column("brand", sqlalchemy.String(255)), sqlalchemy.Column("price", sqlalchemy.Float), sqlalchemy.Column("prod_category", sqlalchemy.String(255)))
products = sqlalchemy.Table("products", metadata, autoload_with=engine)

product_data = [
    {"prod_id": 101, "prod_name": "Sonical M120", "brand": "Sonical", "price": 200, "prod_category": "Mobiles"},
    {"prod_id": 151, "prod_name": "Xtreme X500", "brand": "Xtreme", "price": 450, "prod_category": "Laptops"},
    {"prod_id": 105, "prod_name": "TechnoPad T10", "brand": "TechnoPad", "price": 150, "prod_category": "Tablets"},
    {"prod_id": 107, "prod_name": "AudioMax Z200", "brand": "AudioMax", "price": 80, "prod_category": "Headphones"},
    {"prod_id": 121, "prod_name": "PowerCharge Pro", "brand": "PowerTech", "price": 50, "prod_category": "Accessories"},
    {"prod_id": 123 , "prod_name": "SmartVision S90", "brand": "SmartVision", "price": 700, "prod_category": "TV"},
    {"prod_id": 126, "prod_name": "GamerPro G15", "brand": "GamerPro", "price": 1200, "prod_category": "Gaming Consoles"},
]

with engine.connect() as conn:
    #metadata.create_all(engine)
    #conn.execute(products.insert(),product_data)
    #res = conn.execute(sqlalchemy.text("SELECT * FROM products")).fetchall()
    res = conn.execute(sqlalchemy.select(products)).fetchall()
    print(res)

    #-----------------------------DISTINCT---------------------------------
    print("\n\n\n------------------------------DISTINCT----------------------------------")
    dst_query = conn.execute(sqlalchemy.select(products.c.prod_category.distinct())).fetchall()
    print(dst_query)

    #------------------------------COUNT--------------------------------------------------
    print("\n\n\n------------------------------(FUNC.COUNT)----------------(GROUP_BY)------------------")
    # Number of parameters in select function is equal to Number of prameters in group by function or else it will through the operational error
    dst_query = conn.execute(sqlalchemy.select(users.c.city, sqlalchemy.func.count(users.c.city)).group_by(users.c.city).order_by(users.c.city)).fetchall()
    print(dst_query)

    #-------------------------------------------(GROUP BY)-----------------------------------------------------
    print("\n\n\n------------------------------(FUNC.COUNT)----------------(GROUP_BY)------------------")   
    groupby_query = conn.execute(sqlalchemy.select(products.c.prod_name, sqlalchemy.func.count(products.c.prod_category)).group_by(products.c.prod_name).order_by(products.c.prod_name)).fetchall()
    print(groupby_query)

    print("\n\n\n------------------------------(FUNC.AVG)----------------(GROUP_BY)------------------")   
    groupby_query = conn.execute(sqlalchemy.select(products.c.prod_name, sqlalchemy.func.avg(products.c.price)).group_by(products.c.prod_name).order_by(products.c.prod_name)).fetchall()
    print(groupby_query)

    print("\n\n\n------------------------------(FUNC.MIN)----------------(GROUP_BY)------------------")   
    groupby_query = conn.execute(sqlalchemy.select(products.c.prod_name, sqlalchemy.func.min(products.c.price)).group_by(products.c.prod_name)).fetchall()
    print(groupby_query)

    print("\n\n\n------------------------------(FUNC.MAX)----------------(GROUP_BY)------------------")   
    groupby_query = conn.execute(sqlalchemy.select(products.c.prod_name, sqlalchemy.func.max(products.c.price)).group_by(products.c.prod_name)).fetchall()
    print(groupby_query)


