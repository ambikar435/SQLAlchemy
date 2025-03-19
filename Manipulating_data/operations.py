import sqlalchemy
encoded_password = "Cientra%40123"

url = f"mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/online_shoping?autocommit=True"

engine = sqlalchemy.create_engine(url)
metadata = sqlalchemy.MetaData()
with engine.connect() as conn:
    #conn.execute(sqlalchemy.text("drop table users;"))

    users = sqlalchemy.Table('users', metadata, sqlalchemy.Column('user_id', sqlalchemy.Integer, primary_key=True, autoincrement=False),
                             sqlalchemy.Column("first_name", sqlalchemy.String(255), nullable=False),
                             sqlalchemy.Column("last_name", sqlalchemy.String(255)),
                             sqlalchemy.Column("email_id", sqlalchemy.String(255)),
                             sqlalchemy.Column("city", sqlalchemy.String(255)),
                             sqlalchemy.Column("phone", sqlalchemy.String(255), nullable=False)
                             )
    #metadata.create_all(engine)
    conn.execute(sqlalchemy.text("TRUNCATE table users;"))
    T_tables = conn.execute(sqlalchemy.text("describe users;")).fetchall()
    for i in T_tables:
        print(i)
    user_data = [
        {'user_id': 10, 'first_name': "Claudia", 'last_name': "Sand", 'email_id': "Claudia.Sand@hotmail.com", 'city': "Hanover", 'phone': "+91 111 222 3333"},
        {'user_id': 20, 'first_name': "John", 'last_name': "Doe", 'email_id': "john.doe@gmail.com", 'city': "Berlin", 'phone': "+91 222 333 4444"},
        {'user_id': 15, 'first_name': "Alice", 'last_name': "Brown", 'email_id': "alice.brown@yahoo.com", 'city': "Munich", 'phone': "+91 333 444 5555"},
        {'user_id': 19, 'first_name': "Bob", 'last_name': "Taylor", 'email_id': "bob.taylor@outlook.com", 'city': "Frankfurt", 'phone': "+91 444 555 6666"},
        {'user_id': 11, 'first_name': "Emma", 'last_name': "Watson", 'email_id': "emma.watson@gmail.com", 'city': "Hamburg", 'phone': "+91 555 666 7777"},
        {'user_id': 31, 'first_name': "Liam", 'last_name': "Miller", 'email_id': "liam.miller@hotmail.com", 'city': "Cologne", 'phone': "+91 666 777 8888"},
        {'user_id': 33, 'first_name': "Olivia", 'last_name': "Davis", 'email_id': "olivia.davis@yahoo.com", 'city': "Dusseldorf", 'phone': "+91 777 888 9999"},
        {'user_id': 34, 'first_name': "Noah", 'last_name': "Wilson", 'email_id': "noah.wilson@gmail.com", 'city': "Stuttgart", 'phone': "+91 888 999 0000"},
        {'user_id': 21, 'first_name': "Sophia", 'last_name': "Anderson", 'email_id': "sophia.anderson@outlook.com", 'city': "Leipzig", 'phone': "+91 999 000 1111"},
        {'user_id': 24, 'first_name': "Mason", 'last_name': "Thomas", 'email_id': "mason.thomas@yahoo.com", 'city': "Dortmund", 'phone': "+91 000 111 2222"},
        {'user_id': 17, 'first_name': "Isabella", 'last_name': "Martinez", 'email_id': "isabella.martinez@gmail.com", 'city': "Bremen", 'phone': "+91 111 222 3334"},
        {'user_id': 22, 'first_name': "Ethan", 'last_name': "Garcia", 'email_id': "ethan.garcia@hotmail.com", 'city': "Dresden", 'phone': "+91 222 333 4445"},
        {'user_id': 36, 'first_name': "Ava", 'last_name': "Rodriguez", 'email_id': "ava.rodriguez@gmail.com", 'city': "Nuremberg", 'phone': "+91 333 444 5556"},
        {'user_id': 39, 'first_name': "James", 'last_name': "Hernandez", 'email_id': "james.hernandez@yahoo.com", 'city': "Bochum", 'phone': "+91 444 555 6667"},
        {'user_id': 25, 'first_name': "Charlotte", 'last_name': "Lopez", 'email_id': "charlotte.lopez@outlook.com", 'city': "Bonn", 'phone': "+91 555 666 7778"},
        ]
    conn.execute(users.insert().values(user_data))

    # Select the entire table data
    select_query = sqlalchemy.select(users)
    select_res = conn.execute(select_query).fetchall()
    for i in select_res:
        print(i)

    # Select the perticular column in table
    select_name = sqlalchemy.select(users.c.first_name,)
    select_res_name = conn.execute(select_name).fetchall()
    print(select_res_name)

    # Select the Multiple columns in table
    select_multiple_column = sqlalchemy.select(users.c.first_name, users.c.city).where(users.c.city == 'Berlin')
    select_multiple_query = conn.execute(select_multiple_column).fetchall()
    print(select_multiple_query)

    print("\n\n\n\n")

    # using AND
    condition_and = sqlalchemy.sql.and_(users.c.first_name == "James", users.c.city == 'Bochum')
    condition_and = conn.execute(sqlalchemy.select(users).where(condition_and)).fetchall()
    print(condition_and)

    print("\n\n\n\n")

    # using AND
    condition_or = sqlalchemy.sql.or_(users.c.first_name == "James", users.c.city == 'Bochum')
    condition_or = conn.execute(sqlalchemy.select(users).where(condition_or)).fetchall()
    print(condition_or)