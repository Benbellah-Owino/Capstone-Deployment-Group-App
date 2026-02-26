from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from models import SensorData

app = FastAPI()

templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

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


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    engine_rpm       : int = Form(...),
    lub_oil_pressure : float = Form(...),
    fuel_pressure    : float = Form(...),
    coolant_pressure : float = Form(...),
    lub_oil_temp     : float = Form(...),
    coolant_temp     : float = Form(...),
    engine_condition : bool = Form(...),
):
    data_dict = {
        "engine_rpm": engine_rpm,
        "lub_oil_pressure": lub_oil_pressure,
        "fuel_pressure": fuel_pressure,
        "coolant_pressure": coolant_pressure,
        "lub_oil_temp": lub_oil_temp,
        "coolant_temp": coolant_temp,
        "engine_condition": engine_condition
    }
     
    return templates.TemplateResponse("prediction.html", {"request": request,"data": data_dict})