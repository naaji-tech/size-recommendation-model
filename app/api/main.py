import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.service.recommend_size import recommend_size


# === define the request and response models ===
class BodyMeasurements(BaseModel):
    shoulderBreadth: float
    chestCircumference: float
    waistCircumference: float
    hipCircumference: float
    bicepCircumference: float
    shoulderToCrotchHeight: float
    armLength: float


class GarmentMeasurements(BaseModel):
    sleeveLength: float
    shoulderWidth: float
    chest: float
    waist: float
    bottomCircumference: float
    frontLength: float
    sleeve: float


class GarmentSize(BaseModel):
    XS: GarmentMeasurements
    S: GarmentMeasurements
    M: GarmentMeasurements
    L: GarmentMeasurements
    XL: GarmentMeasurements


class RequestBody(BaseModel):
    userMeasurements: BodyMeasurements
    productMeasurements: GarmentSize
    measurementsWeight: GarmentMeasurements


app = FastAPI()
# === define the API end point ===


@app.post("/v1/sizeRecommendations")
async def size_recommend(request_body: RequestBody):
    """
    API URL end point to size recommendation based on body and garment measurements

    parameters:
    - request_body: RequestBody: Request body containing body measurements and garment sizes

    returns:
    - dict: recommended size
    """
    try:
        user_measurements = request_body.userMeasurements.model_dump()
        garment_sizes = request_body.productMeasurements.model_dump()
        measurement_weight = request_body.measurementsWeight.model_dump()

        rec_size = recommend_size(user_measurements, garment_sizes, measurement_weight)
        print(f"Recommended size: {rec_size}")

        return {"recommendSize": rec_size}

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
