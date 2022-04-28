from typing import List
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Firefox(executable_path="C:/Users/hasan/Desktop/Programming/GeckoDriver/geckodriver.exe")
wait = WebDriverWait(driver, 30)

letters = list(string.ascii_lowercase)

def logInToLinkedIn():
    driver.get("https://www.linkedin.com")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nav__button-secondary"))).click()
    username = "hasanfarhan33@gmail.com"
    password = "5J6NDeyug8PsCgQ"
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button"))).click()

logInToLinkedIn()



driver.quit()