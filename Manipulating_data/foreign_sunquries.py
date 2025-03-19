import sqlalchemy
from datetime import date
encoded_password = "Cientra%40123"

url = f"mysql+pymysql://root:{encoded_password}@127.0.0.1:3306/online_shoping?autocommit=True"

engine = sqlalchemy.create_engine(url)
metadata = sqlalchemy.MetaData()

gold_users = sqlalchemy.Table("gold_users", metadata, sqlalchemy.Column("uid", sqlalchemy.Integer, primary_key = True, autoincrement = False),
                              sqlalchemy.Column("end_date", sqlalchemy.Date, nullable=False),
                              sqlalchemy.Column("points", sqlalchemy.Float))
users = sqlalchemy.Table("users", metadata, autoload_with=engine)

with engine.connect() as conn:
    #metadata.create_all(engine)
    query = conn.execute(sqlalchemy.text("show tables;")).fetchall()
    print(query)
    query = conn.execute(sqlalchemy.text("describe gold_users;")).fetchall()
    for i in query:
        print(i)
    INSERT_VALUES = [
        {"uid": 10, "end_date": date(2025, 5, 15), "points": 1200.5},
        {"uid": 20, "end_date": date(2025, 8, 20), "points": 950.75},
        {"uid": 11, "end_date": date(2024, 12, 31), "points": 2100.0},
        {"uid": 21, "end_date": date(2026, 3, 10), "points": 500.25},
        {"uid": 25, "end_date": date(2025, 11, 5), "points": 1750.9}
    ]
    #conn.execute(gold_users.insert(), INSERT_VALUES)

    print("\n\n\n\n SUB QURIES")

    frgn_key = conn.execute(sqlalchemy.select(users.c.first_name, users.c.last_name, users.c.email_id, users.c.city).where(users.c.user_id.in_(sqlalchemy.select(gold_users.c.uid)))).fetchall()
    for i in frgn_key:
        print(i)
    #*******************************ADDING THE FOREGIN KEY BY ALTRING***************
    res = conn.execute(sqlalchemy.text("SELECT CONSTRAINT_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = 'gold_users' AND COLUMN_NAME = 'uid' AND CONSTRAINT_SCHEMA = 'online_shoping' AND REFERENCED_TABLE_NAME IS NOT NULL")).fetchall()

    if res:
        fk_name = res[0][0]
        conn.execute(sqlalchemy.text(f"ALTER TABLE gold_users DROP FOREIGN KEY {fk_name}"))
        conn.commit()
        print(f"Dropped existing foreign key: {fk_name}")

    # Add new Foreign Key
    conn.execute(sqlalchemy.text("ALTER TABLE gold_users ADD CONSTRAINT fk_uid FOREIGN KEY (uid) REFERENCES users(user_id)"))
    conn.commit()
    print("New foreign key added!")

    # Verify foreign key addition
    res = conn.execute(sqlalchemy.text("SHOW CREATE TABLE gold_users")).fetchall()
    print(res)



