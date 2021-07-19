import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def getPlayer(name):

    full = name.split(" ")

    url = "https://content-api-prod.nba.com/public/1/search/player,page?q=" + full[0]

    for x in full[1:]:
        url += ("%20" + x)
    url += "&page=1"
    html = requests.get(url).text

    y = json.loads(html)
    pid = y["results"]["items"][0]["pid"]

    newurl = "https://www.nba.com/stats/player/" + str(pid)

    driver = webdriver.Firefox()
    driver.get(newurl)

    try:
        w = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "nba-stat-table")))
        tab = driver.find_element_by_class_name("nba-stat-table")

        s = tab.text.split("\n")
        for x in s[1:]:
            t = x.split(" ")

            print(t[0] + " " + t[9])

    except TimeoutException:
        print("Timeout happened no page load")
    driver.close()

player = input("Insert Player Name: ")
if player != "":
    getPlayer(player)