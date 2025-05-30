import requests
from bs4 import BeautifulSoup

def gather_data(topic):
    search_url = f"https://www.google.com/search?q={topic}"
    return f"Sample data for {topic} from Google Search."
