from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

metadata = MetaData()

transactions = Table(
    'transactions', metadata,
    Column('id', Integer, primary_key=True),
    Column('product', String),
    Column('quantity', Integer),
    Column('price', Float),
    Column('total', Float)
)

def init_db(engine):
    metadata.create_all(engine)
