from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL and create an engine
DATABASE_URL = "sqlite:///./wells.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the data model
class Well(Base):
    __tablename__ = "wells"

    id = Column(Integer, primary_key=True, index=True)
    api_well_number = Column(String, index=True)
    production_year = Column(Integer)
    quarter = Column(Integer)
    owner_name = Column(String)
    county = Column(String)
    township = Column(String)
    well_name = Column(String)
    well_number = Column(String)
    oil = Column(Integer)
    gas = Column(Integer)
    brine = Column(Integer)
    days = Column(Integer)

# Create the tables
Base.metadata.create_all(bind=engine)
