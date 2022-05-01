
import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Kainos.db')
Base = declarative_base()


class Elektra(Base):
    __tablename__ = 'Elektra'
    id = Column(Integer, primary_key=True)
    imone = Column('Imone', String)
    kaina = Column('Kaina', String)
    laiko_zonos = Column('Laiko zonos', String)
    planas = Column('Planas', String)
    data = Column('Data', DateTime, default=datetime.datetime.now)

    def __init__(self, imone, kaina, laiko_zonos, planas):
        self.imone = imone
        self.kaina = kaina
        self.laiko_zonos = laiko_zonos
        self.planas = planas

    def __repr__(self):
        return f'{self.id} {self.imone} {self.kaina}  {self.laiko_zonos}  {self.planas}, {self.data}'


Base.metadata.create_all(engine)