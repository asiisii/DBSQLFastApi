from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://user:postgres@localhost:5432/SQLAlchemyFastApi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)  # create engine is responsible for connecting to database using the above url

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
