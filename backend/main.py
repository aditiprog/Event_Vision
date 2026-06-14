from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


data = {
    "status": "No Activity",
    "spikes": 0,
    "saved": 0
}


@app.get("/metrics")
def get_metrics():
    return data


# ADD THIS BELOW /metrics

class Metrics(BaseModel):
    status: str
    spikes: int
    saved: float


@app.post("/update")
def update_metrics(metrics: Metrics):

    data["status"] = metrics.status
    data["spikes"] = metrics.spikes
    data["saved"] = metrics.saved

    return {"message": "updated"}