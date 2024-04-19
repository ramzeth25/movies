from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://{}:{}@localhost:3306/imdb".format('root', 'root12'))
metadata = MetaData()
db_session = scoped_session(sessionmaker(bind=engine))


def init_db():
    metadata.create_all(bind=engine)