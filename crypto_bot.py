crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}
bot_name = "CryptoBuddy"
bot_tone = "🌟 Hey there! I’m CryptoBuddy – your guide to green and growing crypto! Let’s find your best match."

def get_response(user_query):
    query = user_query.lower()

    if "sustainable" in query:
        coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 {coin} is the most eco-friendly crypto with a sustainability score of {crypto_db[coin]['sustainability_score'] * 10}/10!"
    
    elif "trending" in query or "rising" in query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 Trending cryptos: {', '.join(trending)}"

    elif "long-term" in query or "growth" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 0.7:
                return f"🚀 Go for {coin}! It’s rising and highly sustainable – great for long-term growth."

    else:
        return "🤔 I’m still learning. Try asking about sustainability, trending coins, or long-term growth."
print(bot_tone)
print("💬 Ask me something about crypto (type 'exit' to quit):")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("CryptoBuddy: Goodbye and happy investing! 💰")
        break

    response = get_response(user_input)
    print(f"{bot_name}: {response}")
