from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Simran25062@localhost/Fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()