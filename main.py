import threading
import time
import random

# প্রতিটি কয়েনের প্রাথমিক দাম
markets = {
    "BTC": 100.0,
    "VIPS": 25.0,
    "ETH": 20.0,
    "TAL": 30.0,
    "PDD": 10.0,
    "NIO": 5.0,
    "BIDU": 2.0
}

def update_price(coin, action, quantity):
    if coin in markets:
        if action == "BUY":
            markets[coin] += (quantity * 0.50)
        elif action == "SELL":
            markets[coin] -= (quantity * 0.70)
        return markets[coin]
    return None

# ২০ সেকেন্ড পর পর হালকা উঠানামার ফাংশন
def auto_market_fluctuation():
    while True:
        time.sleep(20)  # ২০ সেকেন্ড অপেক্ষা
        for coin in markets:
            # হালকা পরিবর্তন: -০.০২ থেকে +০.০২ পর্যন্ত
            change = random.uniform(-0.02, 0.02)
            markets[coin] = round(markets[coin] + change, 2)
        print(f"বাজার আপডেট হয়েছে: {markets}")

# অটোমেটিক আপডেটার চালু করা
thread = threading.Thread(target=auto_market_fluctuation, daemon=True)
thread.start()

# সাধারণ ট্রেডিং লজিক
print(f"বর্তমান বাজার: {markets}")
