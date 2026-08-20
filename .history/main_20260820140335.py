import joblib
from fastapi import FastAPI

model = joblib.load('Mental_Health_Model.pkl')

