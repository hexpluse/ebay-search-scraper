# ebay-search-scraper

A simple Python script that scrapes eBay listings for any search term, shows item titles and prices, and prints clean URLs to view listings directly.

---

## What it does:

- Searches eBay for a given keyword  
- Displays the first 2 pages of search results  
- Prints each product's:
  - Title  
  - Price  
  - Clean URL (no tracking junk)  

---

How to Use:
query = "whatever you wanna search"
Simply replace the default "GT 1660Ti" placed here, with whatever you want.

---

## Requirements (Make sure you have these installed):

```bash
pip install requests beautifulsoup4 lxml colorama
