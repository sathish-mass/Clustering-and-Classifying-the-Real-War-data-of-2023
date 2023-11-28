from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd   

data = []

service = Service(r"C:\Users\SATHISH\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

with driver:
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s")

    for _ in range(200):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)  # Adjust the sleep duration based on your network speed and page load time

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content #content-text"))):
        data.append(comment.text)

df = pd.DataFrame(data, columns=['comment'])
df.to_csv('data.csv', index=False)
