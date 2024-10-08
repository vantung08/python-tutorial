from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# POSTGRESQL_URL = "postgresql://vantung08:12345678@localhost:5432/python-tutorial-postgresql"
POSTGRESQL_URL = "postgresql://vantung08:12345678@postgresql:5432/python-tutorial-postgresql"

engine = create_engine(POSTGRESQL_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)