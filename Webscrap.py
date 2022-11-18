from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient
from datetime import datetime
#to track when the data is scrapped
dateTimeObj = datetime.now()
# Limited uses likely not a problem for our use case
client = ScrapingAntClient(token='5ba5214582d74c76b36dadb919cb5057')
# Scrape the parking site.
result = client.general_request('https://parkingavailability.charlotte.edu/')

