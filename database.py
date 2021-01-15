#create sql alchemy parts
#no1
from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
'''
import configparser
file='config.ini'
config=configparser.ConfigParser()
config.read(file)

gTYPE=config.get('account ,'db_TYPE')
gUSER=config.get('account','db_USER')
gPASS=config.get('account')
gHOST=config.get('HOST')
gDB=config.get('DB')
'''
'''from dotenv import load_dotenv
import os

load_dotenv()

DB_TYPE=os.environ.get('TYPE')
DB_USER=os.environ.get('USER')
DB_PASS=os.environ.get('PASS')
DB_HOST=os.environ.get('HOST')
DB=os.environ.get('DB')
print(DB)
'''
import configparser
config=configparser.ConfigParser();
config.read(r'C:\Users\KIIT\PycharmProjects\jan\SQLCONNECT\config.ini')
database_type=str(config.get('demo','database_type'))
database_user=str(config.get('demo','database_user'))
database_pass=str(config.get('demo','database_pass'))

database_host=str(config.get('demo','database_host'))

database=str(config.get('demo','database'))

#Create a database URL for SQLAlchemy
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:kiit@localhost/postgres"
SQLALCHEMY_DATABASE_URL = "{}://{}:{}@{}/{}".format(database_type,database_user,database_pass,database_host,database)
#The first step is to create a SQLAlchemy "engine"
#we can also use this in other files.
engine=create_engine(
SQLALCHEMY_DATABASE_URL
)

'''
Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.

But once we create an instance of the SessionLocal class, this instance will be the actual database session.

We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.
'''
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

'''
Now we will use the function declarative_base() that returns a class.

Later we will inherit from this class to create each of the database models or classes (the ORM models):
'''
Base=declarative_base()
