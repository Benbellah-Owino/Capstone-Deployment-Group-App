from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import SensorData

app = FastAPI()

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
def home():
    return """
    <html>
        <head>
            <title>Engine Condition Predictor</title>
        </head>
        <body>
            <h1>Engine Condition Predictor🚀</h1>
                <p>
                    Hello. Welcome to this app where you enter your engine sensor data from
                    your infotainment and we try to predict it.  
                <p/>
        </body>
    </html>
"""

@app.post("/predict")
def predict(data: SensorData):
    return {"payload":data}