from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import json
from dotenv import load_dotenv
import os

load_dotenv()

class EASportsFetch():
    def __init__(self, driver, player_name, site_url):
        self.driver = driver
        self.url = site_url
        self.player_name = player_name
    
    def do_fetch(self):
        try:
            name_arr = self.player_name.split(" ")
            search_param = name_arr[0]
            for i in range(1, len(name_arr)):
                search_param += "+" + name_arr[i]
            self.driver.get(f"{self.url}?search={search_param}")
            player_elements = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr:first-child > td:nth-child(2)")
            if player_elements is None or len(player_elements) == 0:
                return
            player_elements[0].click()
            time.sleep(2)
            columns = self.driver.find_elements(By.CSS_SELECTOR, "#main-content section:nth-child(4) ul")
            attributes = {}
            for c in columns:
                print("This is inside columns loop")
                li_elements = c.find_elements(By.TAG_NAME, "li")
                if li_elements is None or len(li_elements) == 0:
                    continue
                span_elements = li_elements[0].find_elements(By.TAG_NAME, "span")
                if span_elements and len(span_elements) > 1:
                    name = span_elements[0].text.strip()
                    total = span_elements[1].text.strip()
                    try:
                        total = int(total)
                    except ValueError:
                        print("Can't cast value")

                else:
                    name = "---"
                    total = 0  # Or another default value
                
                attributes[name] = {
                    "total": total
                }
                cnt = len(li_elements)

                for i in range(1, cnt):
                    li_element = li_elements[i]
                    span_elements = li_element.find_elements(By.TAG_NAME, "span")
                    if span_elements is None:
                        continue
                    cnt_span = len(span_elements)
                    if span_elements and len(span_elements) > 1:
                        print("THis is  >>>>>>0 " + span_elements[-1].text.strip())
                        key = span_elements[0].text.strip()
                        value = (span_elements[-1].text.strip())
                        try:
                            value = int(value)
                        except ValueError:
                            print("can't cast into integer")
                        attributes[name][key] = value
            print(attributes)
            with open(f"{self.player_name}.json", "w") as file:
                json.dump(attributes, file, indent=4, sort_keys=True)
        except Exception as e:
            print(str(e))

