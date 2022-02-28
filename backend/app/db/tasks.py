from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL



async def connect_to_db(app):
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        app.state._SessionLocal = SessionLocal
    except:
        print("Error fetching database connection")
    finally:
        pass


async def close_db_connection():
    pass