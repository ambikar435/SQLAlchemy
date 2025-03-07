# SQLAlchemy
#installation of sqlalchemy:

pip3 install sqlalchemy --updrade

1. installation command for pymysql(Python mysql client libraray):
---------> pip3 install PyMySql
2. import sqlalchemy
----------
3. creating databse:
-----------engine = create_engine(f'mysql+pymysql://{user}:{encoded_password}@{host_port}/{database_name}')
4. creating table:
-------Persons = Table('persons', metadata,
                Column('user_id', Integer),
                Column('First_name', String(225)),
                Column("last_name", String(225)),
                Column("email_id", String(225)),
                Column("city", String(225)),
                Column('Phone', String(225))
                )
with engine.connect() as connection:
    # Create the table if not exists
    metadata.create_all(engine)

5. display all the database 
----------show databases;
6. display all the tables in database
----------> show tables;
7. INSERT DATA INTO DATABASE TABLE(persons = Table('persons', metadata, Column('user_id', Integer), Column('First_name', String(225)), Column("last_name", String(225)), Column("email_id", String(225)), Column("city", String(225)), Column('Phone', String(225)))
)
---------- Persons.insert().values((data shoud be with list or tuple or dict))
INSERT multiple rows of DATA INTO DATABASE TABLE 
---------connection.execute(persons.insert(),[list of inserted data])

UNIQUE CONSTRAINS AND NOT NULL CONSTRAINS
--------------users = Table("users", metadata, 
              Column('user_id', Integer, nullable=False),
              Column('first_name', String(255), nullable=False),
              Column('last_name', String(255)),
              Column('email_id', String(255)),
              Column('city', String(255)),
              Column('phone', String(255), nullable=False),
              UniqueConstraint('user_id'))

PRIMARY CONSTRAINS:

