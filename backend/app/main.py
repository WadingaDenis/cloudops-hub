from fastapi import FastAPI

app = FastAPI(
    title="CloudOps Hub",
    description="Cloud infrastructure and deployment management platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to CloudOps Hub",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }