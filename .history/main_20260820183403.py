import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
from typing import Literal

model = joblib.load('Mental_Health_Model.pkl')
app = FastAPI()

class StudentData(BaseModel):
      Age                       :    int = Field(ge=10, le=100)
      Gender                    :    Literal['Male', 'Female']
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

top_countires = ['Other','India','USA','Canada','Australia','UK','Germany','Mexico','Turkey','France']

@app.post('/predict')
def predict (data: StudentData):

     country_grp = data.Country if data.Country in top_countires else 'Other'

     input_row = pd.Dataframe([{
          'Age' : data.Age,
          'Gender' : data.Gender,
          'Country' : data.Country,
          'Academic_Level' : data.Academic_Level,
          'Most_Used_Platform' : data.Most_Used_Platform,
          'Purpose_Of_Use' : data.Purpose_Of_Use,
          'Avg_Daily_Usage_Hours' : data.Avg_Daily_Usage_Hours,
          'Daily_Unlocks' : data.Daily_Unlocks,
          'Study_Hours' : data.Study_Hours,
          'Physical_Activity_Hours' : data.Physical_Activity_Hours,
          'Sleep_Hours_Per_Night' : data.Sleep_Hours_Per_Night,
          'Stress_Level' : data.Stress_Level,
          'gourped_countries' : country_grp
          
     }])

     prediction = model.predict(input_row)[0]