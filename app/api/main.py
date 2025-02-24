import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# === define the request and response models ===
class BodyMeasurements(BaseModel):
    shoulder_breadth: float
    chest_circumference: float
    waist_circumference: float
    hip_circumference: float
    bicep_circumference: float
    shoulder_to_crotch_height: float
    arm_length: float


class GarmentMeasurements(BaseModel):
    sleeve_length: float
    shoulder_width: float
    chest: float
    waist: float
    bottom_width: float
    front_length: float
    sleeve: float


class RequestBody(BaseModel):
    body_measurements: BodyMeasurements
    garment_measurements: GarmentMeasurements


app = FastAPI()
# === define the API end point ===


@app.post("/size-recommendation")
async def size_recommend(request_body: RequestBody):
    """
    API URL end point to size recommendation based on body and garment measurements
    """
    try:
        return {"response": "Success", "data": request_body.dict()}

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
