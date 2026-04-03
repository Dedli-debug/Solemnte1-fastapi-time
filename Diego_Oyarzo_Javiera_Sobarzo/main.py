from datetime import datetime
import ntplib
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"mensaje": "Usa /time"}


@app.get("/time")
def time():
    client = ntplib.NTPClient()
    response = client.request("ntp.shoa.cl", version=3)
    ahora = datetime.fromtimestamp(response.tx_time).strftime("%Y-%m-%d %H:%M:%S")
    return {"time": ahora, "source": "SHOA NTP"}