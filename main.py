from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import joblib
import numpy as np

from models import SensorData

app = FastAPI()

templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

model = joblib.load("./predictors/model.pkl")
print(model.n_features_in_)

@app.get("/")
def read_root():
    return {"message":"Hello World"}

# The following fields will be importamt
    # engine_rpm       : int
    # lub_oil_pressure : float
    # fuel_pressure    : float
    # coolant_pressure : float
    # lub_oil_temp     : float
    # coolant_temp     : float 
    # engine_condition : bool

@app.get("/home", response_class=HTMLResponse)
def home(
    request: Request
):
    # data_dict = {
    #     "engine_rpm": engine_rpm,
    #     "lub_oil_pressure": lub_oil_pressure,
    #     "fuel_pressure": fuel_pressure,
    #     "coolant_pressure": coolant_pressure,
    #     "lub_oil_temp": lub_oil_temp,
    #     "coolant_temp": coolant_temp,
    #     "engine_condition": engine_condition
    # }
    data_dict = {}
     
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/prediction")
def home(data = SensorData):
    
    return templates.TemplateResponse("index.html", {"Data": data})


@app.post("/predict")
def predict(
    request: Request,
    # engine_rpm       : int = Form(...),
    # lub_oil_pressure : float = Form(...),
    # fuel_pressure    : float = Form(...),
    # coolant_pressure : float = Form(...),
    # lub_oil_temp     : float = Form(...),
    # coolant_temp     : float = Form(...),
    # engine_condition : bool = Form(...),
    data: SensorData
):
    # data_dict = {
    #     "engine_rpm": engine_rpm,
    #     "lub_oil_pressure": lub_oil_pressure,
    #     "fuel_pressure": fuel_pressure,
    #     "coolant_pressure": coolant_pressure,
    #     "lub_oil_temp": lub_oil_temp,
    #     "coolant_temp": coolant_temp,
    #     "engine_condition": engine_condition
    # }
    

    # Additional features
    oil_pressXtemp = data.lub_oil_pressure * data.lub_oil_temp

     # Convert input to correct feature order
    features = np.array([[
        data.engine_rpm,
        data.lub_oil_pressure,
        data.fuel_pressure,
        data.coolant_pressure,
        data.lub_oil_temp,
        data.coolant_temp,

        #could change
        oil_pressXtemp
    ]])

    prediction = model.predict(features)[0]
    type(prediction)
    print(f"Prediction is: {prediction}")

    return {
        "prediction": int(prediction)
    }


def prediction(request: Request):
    return templates.TemplateResponse("prediction.html", {"request": request,"prediction": prediction})