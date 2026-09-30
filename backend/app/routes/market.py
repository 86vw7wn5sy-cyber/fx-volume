from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.services.data_provider import get_market_snapshot, get_supported_pairs
from app.services.technical_analysis import calculate_analysis

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/pairs")
def get_pairs():
    return {"pairs": get_supported_pairs()}


@router.get("/{symbol}")
def get_symbol_data(symbol: str):
    normalized = symbol.upper()
    if normalized not in get_supported_pairs():
        raise HTTPException(status_code=404, detail=f"Pair '{symbol}' not found")
    snapshot = get_market_snapshot(normalized)
    analysis = calculate_analysis(snapshot)
    return {
        "symbol": normalized,
        "price": snapshot["price"],
        "change_percent": snapshot["change_percent"],
        "volume": snapshot["volume"],
        "trend": analysis["trend"],
        "signals": analysis["signals"],
        "risk": analysis["risk"],
    }


@router.get("/{symbol}/signal")
def get_signal(symbol: str):
    normalized = symbol.upper()
    if normalized not in get_supported_pairs():
        raise HTTPException(status_code=404, detail=f"Pair '{symbol}' not found")

    snapshot = get_market_snapshot(normalized)
    analysis = calculate_analysis(snapshot)
    return {
        "symbol": normalized,
        "summary": analysis["summary"],
        "confidence": analysis["confidence"],
        "entry": analysis["entry"],
        "stop_loss": analysis["stop_loss"],
        "take_profit": analysis["take_profit"],
    }
