import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

webdriver_service = Service("/home/ruizdev7/chromedriver/stable/chromedriver")

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

browser.get("https://cloudbytes.dev")

description = browser.find_element(By.NAME, "description").get_attribute("content")
print(f"{description}")

#Wait for 10 seconds
time.sleep(10)
browser.quit()