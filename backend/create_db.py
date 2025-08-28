from sqlalchemy import create_engine
from models import Base

database_url = "sqlite:///database/users.db"

engine = create_engine(
    database_url
)

Base.metadata.create_all(bind=engine)
