from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import json
from dotenv import load_dotenv
import os

load_dotenv()

class FutBinFetch():
    def __init__(self, driver, player_name, site_url):
        self.driver = driver
        self.url = site_url
        self.player_name = player_name
    
    def do_fetch(self):
        try:
            self.driver.get(self.url)
            search_element = self.driver.find_element(By.CSS_SELECTOR, "header nav form input")
            search_element.send_keys(self.player_name)
            search_element.send_keys(Keys.RETURN)
            time.sleep(2)
        except Exception as e:
            print(str(e))