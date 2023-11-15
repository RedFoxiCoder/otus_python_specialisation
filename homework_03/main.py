from socket import gethostname
from datetime import datetime
from uuid import uuid4
from fastapi import FastAPI, status

app = FastAPI()

@app.get("/")
def root():
    return {"hostname": gethostname(), "timestamp": datetime.now(), "uuid": uuid4()}


@app.get("/isalive", status_code=status.HTTP_200_OK)
def liveness_probe():
    return {"status": "OK"}

@app.get("/ping")
def ping_request():
    return {"message": "pong"}