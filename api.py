# pip install fastapi uvicorn #ye install kro
# then type this in terminal to run: uvicorn api:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "All routes available",
        "routes": {
            "health": "/health",
            "version": "/version",
            "environment": "/environment",
        },
    }


@app.get("/health")
def health_check():
    return {"status": "Up"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}


@app.get("/environment")
def environment():
    return {"environment": "development"}
