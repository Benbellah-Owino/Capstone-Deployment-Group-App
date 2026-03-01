from pydantic import BaseModel 

class SensorData(BaseModel):
    engine_rpm       : int
    lub_oil_pressure : float
    fuel_pressure    : float
    coolant_pressure : float
    lub_oil_temp     : float
    coolant_temp     : float 


class PredictionResponse(BaseModel):
    engine_condition : bool