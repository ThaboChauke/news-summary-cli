import os
import requests
from dotenv import load_dotenv

load_dotenv()

news_api_key = os.getenv("NEWS")


def get_news(api_key):
    url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q=southafrica"
    return requests.get(url)


def process_news(news):

    results = news.json().get("results")



    pass


def main():
    news = get_news(news_api_key)
    process_news(news)



if __name__ == "__main__":
    main()
