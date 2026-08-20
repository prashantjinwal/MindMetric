import joblib
from fastapi import FastAPI

model = joblib.load('Mental_Health_Model.pkl')
app = FastAPI()

@app.get('/')
def geet():
     return {'testing'}

@app.post('/predict')
def predict (data: dict):
     input = {
          'Age',
          'Gender',
          'Country',
          'Academic_Level',
          'Most_Used_Platform',
          'Purpose_Of_Use',
          'Avg_Daily_Usage_Hours',
          'Daily_Unlocks',
          'Study_Hours',
          'Physical_Activity_Hours',
          'Sleep_Hours_Per_Night',
          'Stress_Level',
          'Mental_Health_Score',
          'gourped_countries'
     }