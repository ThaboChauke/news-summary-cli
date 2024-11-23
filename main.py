import os
import requests
from dotenv import load_dotenv

load_dotenv()

news_api_key = os.getenv("NEWS")


URL = f"https://newsdata.io/api/1/latest?apikey={news_api_key}&q=southafrica"
response = requests.get(URL)
print(response.json())