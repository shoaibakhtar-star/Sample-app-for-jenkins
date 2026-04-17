from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Jenkins CI/CD test🚀"}

@app.get("/health")
def health():
    return {"status": "OK"}