import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_name = "../database/tasks.sqlite"
database_dir = os.path.dirname( os.path.realpath(__file__) )
database_url = f"sqlite:///{os.path.join(database_dir, database_name)}"

engine = create_engine(database_url)

Session = sessionmaker(engine)

Base = declarative_base()
