import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

def get_news():
   try:
      api_key = os.getenv("NEWS_API_KEY")
      url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey={api_key}"
      response = requests.get(url)
      response.raise_for_status()
      news = response.json()
      
      articles = news.get("articles", [])

      print("\nTop 3 U.S. Business News Headlines:\n")
      for i, article in enumerate(articles, start=1):
         print(f"{i}. {article.get("title")} - {article.get("source", {}).get("name")}")

      log_action("News fetched successfully", True)

   except Exception as e:
      log_action(f"Failed to fetch news: {e}", False)
      print("Error getting news.")
      
def log_action(message, success):
   with open("logs.txt", "a") as log_file:
      status = "SUCCESS" if success else "FAILURE"
      log_file.write(f"{datetime.now()} - {status}: {message}\n")
