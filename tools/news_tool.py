import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NewsTool:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        if not self.api_key:
            raise ValueError("NEWS_API_KEY not found")

        self.base_url = "https://newsapi.org/v2/top-headlines"
    def get_news(self, topic: str, limit: int = 5):
        params = {
            "category": topic,        # IMPORTANT FIX
            "pageSize": limit,
            "apiKey": self.api_key,
            "language": "en",
            "country": "us"
        }
        response = requests.get(self.base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        articles = []
        for article in data.get("articles", []):
            articles.append({
                "title": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "description": article.get("description"),
                "url": article.get("url")
            })
        return articles
