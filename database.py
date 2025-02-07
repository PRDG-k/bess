from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime
from dotenv import load_dotenv
import os

load_dotenv("config.env")
password = os.getenv("password")

DATABASE_URL = f"postgresql+psycopg2://postgres:{password}@127.0.0.1:5432/energy_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class EnergyData(Base):
    __tablename__ = "energy_data"
    time = Column(DateTime, primary_key=True, default=datetime.datetime.utcnow)
    solar_pred = Column(Float)
    load_pred = Column(Float)
    ess_charge = Column(Float)
    ess_discharge = Column(Float)

Base.metadata.create_all(bind=engine)

def save_to_db(data):
    session = SessionLocal()
    entry = EnergyData(
        time=datetime.datetime.strptime(data["time"], "%Y-%m-%d %H:%M:%S"),
        solar_pred=data["solar_pred"],
        load_pred=data["load_pred"],
        ess_charge=data["ess_schedule"]["charge"],
        ess_discharge=data["ess_schedule"]["discharge"]
    )
    session.add(entry)
    session.commit()
    session.close()

def get_latest_data():
    session = SessionLocal()
    result = session.query(EnergyData).order_by(EnergyData.time.desc()).first()
    session.close()
    return result
