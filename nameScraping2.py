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

def searchAndFetchNames(letters):
    names = []
    pageCount = 1
    for i in range(len(letters)):
        searchBar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-global-typeahead__input')))
        searchBar.send_keys(letters[i])
        searchBar.send_keys(Keys.RETURN)
        if i == 0:
            time.sleep(5)
            peopleButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[2]/section/div/nav/div/ul/li/button[contains(@aria-label, "People")]')))
            peopleButton.click()
        usersList = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/ul')))
        userResults = usersList.find_elements_by_tag_name('li')
        # print(userResults)

        currentPageNames = []
        for user in userResults:
            currentPageNames.append(user.find_elements_by_css_selector('div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)'))

        # Moving to the next page
        if len(currentPageNames) >= 10:
            for i in range(len(currentPageNames)):
                names.append(currentPageNames[i][0].text)
                pageCount+=1
            #TODO: Go to next page here, and increase page count. Then clear currentPageNames
            if pageCount <= 2:
                nextButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[5]/div/div/ul/li[{}]/button'.format(pageCount))))
                nextButton.click()
            else:
                nextButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div/div[2]/div/ul/li[{}]/button'.format(pageCount))))
                nextButton.click()
            currentPageNames.clear()

        time.sleep(5)
        searchBar.clear()
        break


searchAndFetchNames(letters)
# driver.quit()