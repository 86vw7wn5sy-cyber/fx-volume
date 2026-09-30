from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes.market import router as market_router

app = FastAPI(
    title="FX Volume",
    description="Forex AI Analysis Platform",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(market_router, prefix="/api/v1")


@app.get("/health")
def healthcheck() -> dict:
    return {"status": "ok", "service": "fx-volume"}
