import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

model = joblib.load('Mental_Health_Model.pkl')
app = FastAPI()

class StudentData(BaseModel):
      Age                       :    int  
      Gender                    :    str 
      Country                   :    str 
      Academic_Level            :    str 
      Most_Used_Platform        :    str 
      Purpose_Of_Use            :    str 
      Avg_Daily_Usage_Hours     :   float
      Daily_Unlocks             :   int
      Study_Hours               :   float
      Physical_Activity_Hours   :   float
      Sleep_Hours_Per_Night     :   float
      Stress_Level              :   str 
      



@app.get('/')
def geet():
     return {'testing'}

@app.post('/predict')
def predict (data: StudentData):
     input_row = pd.Dataframe([{
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
     }])