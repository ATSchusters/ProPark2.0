from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

options.headless = True

url = 'https://parkingavailability.charlotte.edu/'

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

driver.get(url)

elements = driver.find_elements(By.TAG_NAME, 'app-percentage')

#for title in elements:
#    heading = title.find_element(By.CLASS_NAME, 'green ng-star-inserted').text
#    print(heading)
