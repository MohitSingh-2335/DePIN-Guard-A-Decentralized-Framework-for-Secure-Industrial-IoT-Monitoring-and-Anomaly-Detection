from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "project": "DePIN-Guard",
        "status": "Backend is Live",
        "team_lead": "Priyanshu"
    }
