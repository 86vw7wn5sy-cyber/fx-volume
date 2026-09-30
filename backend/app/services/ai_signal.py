from typing import Dict


def analyze_symbol(snapshot: Dict) -> Dict:
    price = float(snapshot["price"])
    change = float(snapshot["change_percent"])
    volume = int(snapshot["volume"])

    bias = "buy" if change >= 0 else "sell"
    confidence = 0.57 + min(abs(change / 5), 0.25) + (0.1 if volume > 10000 else 0)
    confidence = max(0.55, min(0.92, round(confidence, 2)))

    return {
        "symbol": snapshot["symbol"],
        "bias": bias,
        "confidence": confidence,
        "summary": (
            f"The model sees a {bias.upper()} bias for {snapshot['symbol']} "
            f"because the market shows {change}% momentum and healthy volume."
        ),
        "entry": round(price, 5 if price < 2 else 3),
        "stop_loss": round(price * 0.995, 5 if price < 2 else 3),
        "take_profit": round(price * 1.012, 5 if price < 2 else 3),
    }
