import joblib
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load('Mental_Health_Model.pkl')
app = FastAPI()

class StudentData:
     


@app.get('/')
def geet():
     return {'testing'}

@app.post('/predict')
def predict (data: dict):
     pass 