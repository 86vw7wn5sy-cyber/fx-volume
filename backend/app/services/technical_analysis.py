def calculate_analysis(snapshot: dict) -> dict:
    price = float(snapshot["price"])
    change = float(snapshot["change_percent"])
    volume = int(snapshot["volume"])
    hist = snapshot["history"]
    recent = hist[-5:]
    trend = "Bullish" if price > sum(hist[:-1]) / len(hist[:-1]) else "Bearish"
    if abs(change) < 0.2:
        trend = "Neutral"

    rsi = 50 + (sum(recent) - min(recent) * 2) / max(len(recent), 1)
    rsi = max(0, min(100, rsi))

    signals = {
        "rsi": round(rsi, 2),
        "trend": trend,
        "volume_strength": "High" if volume > 10000 else "Normal",
        "momentum": "Strong" if change > 0 else "Weak",
    }

    summary = (
        f"{snapshot['symbol']} shows a {trend.lower()} posture with a "
        f"{signals['momentum'].lower()} momentum and {signals['volume_strength'].lower()} volume."
    )

    confidence = 0.61 + (abs(change) / 10) + (1 if signals["volume_strength"] == "High" else 0)
    confidence = max(0.52, min(0.94, round(confidence, 2)))

    risk = {
        "risk_level": "Moderate" if confidence < 0.75 else "Aggressive",
        "stop_loss": round(price * 0.995, 5 if price < 2 else 3),
        "take_profit": round(price * 1.01, 5 if price < 2 else 3),
    }

    return {
        "trend": trend,
        "signals": signals,
        "risk": risk,
        "summary": summary,
        "confidence": confidence,
        "entry": round(price, 5 if price < 2 else 3),
        "stop_loss": risk["stop_loss"],
        "take_profit": risk["take_profit"],
    }
