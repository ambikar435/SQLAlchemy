import sqlalchemy
encoded_password = "Cientra%40123"

url = f"mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/online_shoping?autocommit=True"

engine = sqlalchemy.create_engine(url)

metadata = sqlalchemy.MetaData()

with engine.connect() as conn:
    T_tables = conn.execute(sqlalchemy.text("show tables")).fetchall()
    print(T_tables)
    #************************CREATE TABLE***************************************
    products = sqlalchemy.Table('Products', metadata, sqlalchemy.Column("Name", sqlalchemy.String(225)), sqlalchemy.Column("Price", sqlalchemy.Integer), sqlalchemy.Column("Discount", sqlalchemy.Integer))
    #metadata.create_all(engine) # Creating the Table
    table_details = conn.execute(sqlalchemy.text("describe Products;")).fetchall()
    print(table_details)
    #************************TRUNCATE THE TABLE*******************************
    #table_details = conn.execute(sqlalchemy.text("TRUNCATE TABLE Products;"))
    
    #***********************INSERT DATA INTO TABLE****************************s
    """
    conn.execute(products.insert(), [
        {'Name': 'speakers', 'Price':70, 'Discount':15},
        {'Name': 'headphones', 'Price':100, 'Discount':0},
        {'Name': 'mouse', 'Price':20, 'Discount':0},
        {'Name': 'keyboard', 'Price':15, 'Discount':0}
    ])"
    """
    #***update the Discount cloumn by 20% of price
    #conn.execute(products.update().values(Discount = 0.2 * products.c.Price))

    #***************update the Discount column to 0
    #conn.execute(products.update().values(Discount = 0))

    #*****uppdate the Multiple columns*****************
    #conn.execute(products.update().values(Discount = 0.2 * products.c.Price, Price = 1.1 * products.c.Price))
    # which update will happen first: first it will update price late the discount bacuse in database Table we have price cloumn first
    select_query = sqlalchemy.select(products)
    res_query = conn.execute(select_query).fetchall()
    for i in res_query:
        print(i)