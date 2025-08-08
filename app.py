from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware 
from fastapi import HTTPException
from textSummarizer.pipeline.prediction  import PredictionPipeline

text:str = "What is Text Summarization?"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/",tags =["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")
    

@app.post("/predict")
async def predict(text: str, min_length: int = 30, max_length: int = 120):
    if min_length <= 0 or max_length <= 0:
        raise HTTPException(status_code=400, detail="min_length and max_length must be positive integers.")
    if min_length >= max_length:
        raise HTTPException(status_code=400, detail="max_length must be greater than min_length.")

    try:
        prediction_pipeline = PredictionPipeline()
        summary = prediction_pipeline.predict(text, min_length=min_length, max_length=max_length)
        return {"summary": summary}
    except Exception as e:
        return Response(f"Error Occurred! {e}")