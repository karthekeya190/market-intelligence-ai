import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage,HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatOpenAI(model="gpt-4",temperature=0.3)
def generate_insight_from_articles(file_path="data/processed/cleaned_articles.csv"):
    df = pd.read_csv(file_path)

    # Combine article titles or summaries into a prompt
    joined_titles = "\n".join(f"- {row['title']}" for _, row in df.iterrows())

    prompt = f"""
    These are the latest TechCrunch article titles related to a market query. Based on them, summarize current trends, highlight emerging companies, and any shifts in strategy or product innovation.

    Articles:
    {joined_titles}
    """

    messages = [
        SystemMessage(content="You are a senior market research analyst."),
        HumanMessage(content=prompt)
    ]

    response = llm(messages)
    return response.content