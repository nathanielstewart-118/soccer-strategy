from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import json
from dotenv import load_dotenv
import os

load_dotenv()


class FMInsideFetch():
    def __init__(self, driver, player_name, site_url):
        self.driver = driver
        self.url = site_url
        self.player_name = player_name

    def do_fetch(self):
        try:
            self.driver.get(self.url)
            search_element = self.driver.find_element(By.NAME, "name")
            search_element.send_keys(self.player_name)
            search_element.send_keys(Keys.RETURN)
            time.sleep(2)
            a_elements = self.driver.find_elements(By.CSS_SELECTOR, "#player_table .players > ul:first-child a")
            if a_elements is None or len(a_elements) == 0:
                return
            a_elements[0].click()
            
            print("This is before get version elements")
            version_elements = self.driver.find_elements(By.CSS_SELECTOR, "#main_body .player_versions > li > a")
            print(version_elements)
            attributes = {}
            ve_cnt = len(version_elements)
            for i in range(ve_cnt):
                version_element = version_elements[i]
                print("THis is inside for loop")
                version_element.click()
                version_elements = self.driver.find_elements(By.CSS_SELECTOR, "#main_body .player_versions > li > a")
                print("This is after lcick version element")
                player_stats_element = self.driver.find_elements(By.ID, "player_stats")
                print(player_stats_element)
                if player_stats_element is None or len(player_stats_element) == 0:
                    continue
                columns = self.driver.find_elements(By.CSS_SELECTOR, "#player_stats .column")
                for c in columns:
                    print("This is inside columns loop")
                    name_elements = c.find_elements(By.TAG_NAME, "h3")
                    name = "___" 
                    total = 0
                    if name_elements is not None and len(name_elements) > 0:
                        name = name_elements[0].text.split("\n")[0]
                        value_elements = name_elements[0].find_elements(By.TAG_NAME, "span")
                        total = int(value_elements[0].text) if value_elements is not None and len(value_elements) > 0 else 0
                    attributes[name] = {
                        "total": total
                    }

                    tr_elements = c.find_elements(By.TAG_NAME, "tr")
                    for tr in tr_elements:
                        td_elements = tr.find_elements(By.TAG_NAME, "td")
                        attributes[name][td_elements[0].text.strip()] = int(td_elements[1].text.strip())
                break

            return attributes
        except Exception as e:
            print(str(e))
