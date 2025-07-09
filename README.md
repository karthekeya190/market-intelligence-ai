# 🤖 AI-Powered Market Research Analyst

An intelligent AI system that scrapes market news, analyzes trends using GPT-4/Claude 3, and delivers real-time insights via an interactive dashboard.

---

## 🚀 What It Does

- 🔍 **Scrapes** TechCrunch for articles on any market topic
- 🧹 **Cleans** and structures data automatically
- 🧠 **Generates insights** using GPT-4 (or Claude 3)
- 📊 **Displays** everything in a Streamlit dashboard

---

## 🛠️ Tech Stack

**Scraping**: Scrapy, BeautifulSoup  
**Cleaning**: Pandas, NumPy  
**LLM Analysis**: LangChain + GPT-4 + Claude 3  
**UI**: Streamlit, Plotly  
**Future**: LangGraph, PostgreSQL, BigQuery

---

## ⚙️ Getting Started

```bash
git clone https://github.com/karthekeya190/market-intelligence-ai.git
cd market-intelligence-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Create a .env file:

```bash
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-claude-key  # optional
```
## Run the app:

```bash
streamlit run app/visualizer/dashboard.py
```
