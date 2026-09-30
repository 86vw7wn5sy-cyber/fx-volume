from fastapi import FastAPI

app = FastAPI(title="FX Volume API")


@app.get("/")
def root():
    return {"message": "FX Volume API is running"}
