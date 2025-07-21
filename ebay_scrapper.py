import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from urllib.parse import unquote
import time
import random


# Initialize colorama
init(autoreset=True)

# Product to search
query = "GT 1660Ti"
base_url = "https://www.ebay.com/sch/i.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection": "keep-alive",
    "DNT": "1"
}

print(f"\nSearch results for: {query}\n")

item_count = 0

for page in range(1, 3):  # pages 1 and 2
    print(f"🔄 Page {page}")

    # Build new URL for each page
    url = f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ', '+')}&_sop=12&_pgn={page}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    items = soup.select(".s-item")

    for item in items:
        title = item.select_one(".s-item__title")
        price = item.select_one(".s-item__price")
        link = item.select_one(".s-item__link")

        if title and price and link and "Shop on eBay" not in title.text:
            clean_url = link['href'].split("?")[0]
            print(f"{item_count+1:02}. {title.text.strip()} - {Fore.GREEN}{price.text.strip()}{Style.RESET_ALL}")
            print(f"🔗 View on eBay: {clean_url}\n")
            item_count += 1

    time.sleep(random.uniform(1.5, 3.5))
