from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from model import SessionLocal, Well

# Create a FastAPI instance
app = FastAPI()

# Dependency to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/wells/{api_well_number}")
def read_wells(api_well_number: str, db: Session = Depends(get_db)):
    # Query the database for records with the given api_well_number
    wells = db.query(Well).filter(Well.api_well_number == api_well_number).all()
    if not wells:
        raise HTTPException(status_code=404, detail="Wells not found")

    # Calculate the sums of oil, gas, and brine
    total_oil = sum(well.oil for well in wells)
    total_gas = sum(well.gas for well in wells)
    total_brine = sum(well.brine for well in wells)

    return {
        "api_well_number": api_well_number,
        "total_oil": total_oil,
        "total_gas": total_gas,
        "total_brine": total_brine
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
