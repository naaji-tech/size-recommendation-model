import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.service.recommend_size import recommend_size


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


class GarmentSize(BaseModel):
    XS: GarmentMeasurements
    S: GarmentMeasurements
    M: GarmentMeasurements
    L: GarmentMeasurements
    XL: GarmentMeasurements


class RequestBody(BaseModel):
    body_measurements: BodyMeasurements
    garment_size_and_measurements: GarmentSize


app = FastAPI()
# === define the API end point ===


@app.post("/size-recommendation")
async def size_recommend(request_body: RequestBody):
    """
    API URL end point to size recommendation based on body and garment measurements

    parameters:
    - request_body: RequestBody: Request body containing body measurements and garment sizes

    returns:
    - dict
    """
    try:
        user_measurements = request_body.body_measurements.model_dump()
        garment_sizes = request_body.garment_size_and_measurements.model_dump()

        rec_size = recommend_size(user_measurements, garment_sizes)

        return {"recommend_size": rec_size}

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
