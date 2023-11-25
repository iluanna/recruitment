from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.config import SQL_DATABASE_NAME
from .json import DbEntity

Base = declarative_base()

class Exchange(Base):
    __tablename__ = 'currency_rates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    currency = Column(String(3))
    rate = Column(Float)
    price_in_pln = Column(Float)
    date = Column(String(10))


class SqlDatabaseConnector: 
    def __init__(self) -> None:
        self.engine = create_engine(f"sqlite:///{SQL_DATABASE_NAME}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, entity: dict) -> None:
        new_exchange = Exchange(**entity)
        with self.Session() as session:
            session.add(new_exchange)
            session.commit()

    def get_all(self) -> list[DbEntity]:
        with self.Session() as session:
            exchanges = session.query(Exchange).all()
        db_entities = [DbEntity(id=exchange.id, currency=exchange.currency, rate=exchange.rate,
                        price_in_pln=exchange.price_in_pln, date=exchange.date) for exchange in exchanges]
        return db_entities

    def get_by_id(self, id: int) -> DbEntity:
        with self.Session() as session:
            exchange = session.get(Exchange, id)
        if exchange is None:
            raise Exception(f"Missing object with id: {id}")
        else:
            obj = DbEntity(id=exchange.id, currency=exchange.currency, rate=exchange.rate,
                        price_in_pln=exchange.price_in_pln, date=exchange.date)
        return obj
