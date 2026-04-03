from datetime import datetime
import ntplib
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"mensaje": "Usa /time"}


@app.get("/time")
def time():
    try:
        client = ntplib.NTPClient()
        response = client.request("ntp.shoa.cl", version=3)
        ahora = datetime.fromtimestamp(response.tx_time).strftime("%Y-%m-%d %H:%M:%S")
        return {"time": ahora, "source": "SHOA NTP"}
    except Exception as e:
        return {"error": "No se pudo obtener la hora oficial", "detalle": str(e)}