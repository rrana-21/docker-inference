from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI()
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class InputData(BaseModel):
    text: str

#sends post request for predict
@app.post("/predict")
def predict(data: InputData):
    result = model(data.text)
    return {"prediction": result}
