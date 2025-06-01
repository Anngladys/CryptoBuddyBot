
🪙 Step-by-Step Guide – CryptoBuddy Chatbot

1. Design the Chatbot’s Personality
	•	Name: CryptoBuddy
	•	Tone: Friendly and emoji-rich
	📝 We chose a friendly tone to make the experience more accessible for crypto beginners. It adds fun and energy to the conversation.

2. Predefined Crypto Data

We used a predefined dictionary with 3 cryptocurrencies:

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

	📝 The data helped us simulate a basic AI advisor using simple values for trend and sustainability.

3. Chatbot Logic

User Input Examples:
	•	“Which crypto is trending up?”
	•	“What’s the most sustainable coin?”
	•	“Which one is good for long-term growth?”

Bot Logic:

if "sustainable" in query:
    # Recommend crypto with highest sustainability score
elif "trending" in query or "rising" in query:
    # List all cryptos with "rising" trend
elif "long-term" in query or "growth" in query:
    # Combine sustainability + trend
else:
    # Default fallback response

	📝 This logic shows how rule-based decision-making works — simple but effective.

4. Add Advice Rules
	•	Profitability Rule: Recommend cryptos with "rising" price trend and "high" market cap.
	•	Sustainability Rule: Recommend coins with "low" energy use and score > 7/10.

	📝 These rules mimic how an expert might evaluate crypto choices with basic criteria.

5. Test Your Bot

Sample Conversation:

You: Which crypto should I buy for long-term growth?
CryptoBuddy: Cardano (ADA) is trending up and has a top-tier sustainability score! 🚀

🧠 Our Custom Chatbot Logic (Added Notes)

We created three intelligent branches:
	•	Sustainability-based recommendation
	•	Trend-based listing
	•	Combined logic for long-term growth

	📝 The use of if-else logic gives our chatbot decision-making ability similar to a basic AI model.

📽 Submission Notes
	•	✅ Python file with chatbot logic included
	•	✅ Sample data used and explained
	•	✅ This file includes enhanced documentation
	•	📝 Suggested improvement: Add screenshots or video recording for final submission

📝 Reflections

Working on this chatbot helped us understand the foundation of AI-driven logic and how simple rules can create helpful interactions. The mix of creativity (tone + conversation) and logic (rules + data) made the project really engaging.

✅ Ethics Note

Disclaimer: 💡 Crypto is risky — always do your own research before investing!
