from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
import models

db_user: str = 'postgres'
db_port: int = 5432
db_host: str = 'localhost'
db_password: str = '2021'
db_table: str = 'edudu'

DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_table}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

models.Base.metadata.create_all(bind=engine)






