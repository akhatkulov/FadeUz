from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,BigInteger, func
from sqlalchemy.orm import sessionmaker, declarative_base

url_l="postgresql://postgres:1945@localhost/postgres"

engine = create_engine(url_l)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user_fade'
    id = Column(Integer,primary_key=True,autoincrement=True)
    cid = Column(BigInteger,unique=True,nullable=False)
    ism = Column(String)
    tel = Column(String)
    nav = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_user(cid):
    try:
        x = User(cid=cid,ism=" ",tel=" ",nav=" ")
        session.add(x)
        session.commit()
    except:
        session.rollback()

def put_name(cid,name):
    x = session.query(User).filter_by(cid=int(cid)).first()
    x.ism = name
    session.commit()

def put_tel(cid,tel):
    x = session.query(User).filter_by(cid=int(cid)).first()
    x.tel = tel
    session.commit()

def put_nav(cid,nav):
    x = session.query(User).filter_by(cid=int(cid)).first()
    x.nav = nav
    session.commit()

def get_name(cid):
    x = session.query(User).filter_by(cid=int(cid)).first()
    return x.ism

def get_tel(cid):
    x = session.query(User).filter_by(cid=int(cid)).first()
    return x.tel

def get_nav(cid):
    x = session.query(User).filter_by(cid=int(cid)).first()
    return x.nav