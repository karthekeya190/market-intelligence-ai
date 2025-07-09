from app.analyzer.insights_agent import generate_insight_from_articles

if __name__ == "__main__":
    insight = generate_insight_from_articles()
    print("\n🔍 MARKET INSIGHTS:\n")
    print(insight)
