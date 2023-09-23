from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()

OWNER = os.getenv("OWNER")
PASSWORD = os.getenv("PASSWORD")
DB_NAME = os.getenv("DB_NAME")
SERVER = os.getenv("SERVER")

SQLALCHEMY_DATABASE_URL = f"postgresql://{OWNER}:{PASSWORD}@{SERVER}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)  # create engine is responsible for connecting to database using the above url

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
