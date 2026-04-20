from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Jenkins CI/CD test3 final test 🚀 Automation"}

@app.get("/health")
def health():
    return {"status": "OK"}