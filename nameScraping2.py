from typing import List
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from colorama import Fore, Back, Style, init
init(autoreset=True)

import time

driver = webdriver.Firefox(executable_path="C:/Users/hasan/Desktop/Programming/GeckoDriver/geckodriver.exe")
wait = WebDriverWait(driver, 45)
actions = ActionChains(driver)

letters = list(string.ascii_lowercase)

def logInToLinkedIn():
    driver.get("https://www.linkedin.com")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nav__button-secondary"))).click()
    username = "hasanfarhan33@gmail.com"
    password = "5J6NDeyug8PsCgQ"
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button"))).click()

def scrollDown():
    lastHeight = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)
        newHeight = driver.execute_script('return document.body.scrollHeight')
        if newHeight == lastHeight:
            break
        lastHeight = newHeight

def seeIfAnElementExistsOrNot(elementName):
    if elementName:
        print("Yea, exists")
    else:
        print("Nah man, you blind")


#TODO: Handle unable to search error
def searchAndFetchNames(letters):
    names = []
    for i in range(len(letters)):
        pageCount = 1
        searchBar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.search-global-typeahead__input')))
        searchBar.send_keys(letters[i])
        searchBar.send_keys(Keys.RETURN)
        if i == 0:
            time.sleep(5)
            peopleButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[2]/section/div/nav/div/ul/li/button[contains(@aria-label, "People")]')))
            peopleButton.click()
        time.sleep(2)

        while pageCount <= 100:
            time.sleep(5)
            usersList = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul')))
            userResults = usersList.find_elements_by_tag_name('li')
            # print("User Results:", userResults)

            currentPageNames = []
            for user in userResults:
                currentPageNames.append(user.find_elements_by_css_selector('div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)'))

            # print("Current Page Names:", currentPageNames)

            # Appending currentPageNames into the names list
            if len(currentPageNames) >=10:
                for i in range(len(currentPageNames)):
                    names.append(currentPageNames[i][0].text)
                currentPageNames.clear()

            # GOING TO THE NEXT PAGE
            time.sleep(2)
            pageCount += 1
            scrollDown()
            buttonsDiv = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.artdeco-pagination.artdeco-pagination--has-controls.ember-view.pv5.ph2')))
            buttonList = buttonsDiv.find_element_by_css_selector('.artdeco-pagination__pages')
            buttonString = '[aria-label="Page {}"]'.format(pageCount)
            driver.find_element_by_css_selector(buttonString).click()
            print("NAMES HERE: ", names)
            print("Page No: ", pageCount)
        # continue

        break
        time.sleep(5)
        searchBar.clear()


logInToLinkedIn()
searchAndFetchNames(letters)
# driver.quit()