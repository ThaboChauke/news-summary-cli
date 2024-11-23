import os
import requests
from dotenv import load_dotenv

load_dotenv()
news_api_key = os.getenv("NEWS")

def get_news(api_key):
    url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q=southafrica"
    return requests.get(url)

def process_news(news):
    headlines = []
    results = news.json().get("results")
    for result in results:
        headlines.append(dict(title=result["title"], url=result["link"]))

    return headlines

def main():
    news = get_news(news_api_key)
    headlines = process_news(news)

    print("\n---------------------------->Latest Headlines<----------------------------\n")

    for headline in enumerate(headlines, start=1):

        print(headline[0] , ". HEADLINE: " + headline[1].get("title") + "\n"
              + "LINK TO ARTICLE: " + headline[1].get("url") + "\n")

    print("\n---------------------------->END<----------------------------\n")

if __name__ == "__main__":
    main()
