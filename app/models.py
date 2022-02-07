# coding=utf-8
from sqlalchemy import create_engine, Integer, Column, String, delete
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import sessionmaker, declarative_base
import logging as lg


# je crée une nouvelle machine qui indique à l'orm où se trouve la base de données
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# gestionnaire de base de données
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(), nullable=False)
    poster = Column(String(), nullable=False)


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    content1 = Content(name='Harry Potter', description='Je suis une description de harry Potter', poster='https://th.bing.com/th/id/R.179ac444e7ccf75512ea22b0493b5087?rik=sAE87XMQFabWLQ&pid=ImgRaw&r=0')
    content2 = Content(name='Orient', description='je suis une description de orient', poster='https://th.bing.com/th/id/R.179ac444e7ccf75512ea22b0493b5087?rik=sAE87XMQFabWLQ&pid=ImgRaw&r=0')

    session.add_all([content1, content2])
    session.commit()
    lg.warning('LA BASE DE DONNEES EST INITIALISE')


