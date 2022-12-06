from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# creates an options object so we can mess with chromes settings
options = webdriver.ChromeOptions()

# Makes the tab hidden
options.headless = True

# URL of the website to be scrapped
url = 'https://parkingavailability.charlotte.edu/'

# This is what scrapes the page
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

# Commands the driver to the appropriate url
driver.get(url)

# This grabs the tab which contains the information we want
elements = driver.find_elements(By.CLASS_NAME, 'mat-list-item-content')

list = []
# for loop to get the numbers and deck name
for title in elements:
   number = title.find_element(By.TAG_NAME, 'app-percentage').text
   name = title.find_element(By.CLASS_NAME, 'deck-name').text
   list.append([number, name])
