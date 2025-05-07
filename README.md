# Web Scraping and Data Entry Project

A Python automation project that scrapes rental property data from a Zillow clone website and automatically enters it into a Google Form.

## Features

- Scrapes property listings including:
  - Property addresses
  - Rental prices
  - Listing URLs
- Automatically fills a Google Form with the scraped data
- Uses BeautifulSoup for web scraping
- Uses Selenium WebDriver for form automation

## Requirements

- Python 3.11
- BeautifulSoup4
- Selenium
- Requests

## How It Works

1. The script scrapes property data from a Zillow clone website
2. For each property listing, it extracts:
   - Property address
   - Rental price
   - Listing URL
3. Using Selenium, it automatically fills out a Google Form with the collected data
4. The process repeats for all scraped listings

## Setup

1. Install the required dependencies:
```sh
pip install beautifulsoup4 selenium requests
```

2. Make sure you have Chrome WebDriver installed

3. Run main.py