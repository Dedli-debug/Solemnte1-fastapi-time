from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Usa /time"}

@app.get("/time")
def time():
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"time": ahora}