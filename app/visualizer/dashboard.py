import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))




import streamlit as st
import pandas as pd
from app.scraper.scraper import run_scraper
from app.cleaner.cleaner import clean_scraped_data
from app.analyzer.insights_agent import generate_insight_from_articles

def main():
    st.title("📊 AI-Powered Market Research Analyst")

    query = st.text_input("Enter a market topic:", value="AI")
    if st.button("Analyze"):
        with st.spinner("Scraping latest articles..."):
            run_scraper(query)

        with st.spinner("Cleaning data..."):
            df = clean_scraped_data()

        st.success("✅ Data ready!")

        st.subheader("🔗 Scraped Articles")
        for _, row in df.iterrows():
            st.markdown(f"- [{row['title']}]({row['url']})")

        with st.spinner("Generating insights with GPT..."):
            insights = generate_insight_from_articles()

        st.subheader("📌 Market Insights")
        st.markdown(insights)

if __name__ == "__main__":
    main()
