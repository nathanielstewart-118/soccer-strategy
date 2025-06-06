from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(100)
driver.get("https://fminside.net/players")  # Replace with the actual URL

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        });
        window.chrome = {
          runtime: {}
        };
    """
})



def get_attributes_from_fminside(driver):
    try:

        search_element = driver.find_element(By.NAME, "name")
        search_element.send_keys("Paulo Dybala")
        search_element.send_keys(Keys.RETURN)
        time.sleep(2)
        a_elements = driver.find_elements(By.CSS_SELECTOR, "#player_table .players > ul:first-child a")
        if a_elements is None or len(a_elements) == 0:
            return
        a_elements[0].click()
        
        print("This is before get version elements")
        version_elements = driver.find_elements(By.CSS_SELECTOR, "#main_body .player_versions > li > a")
        print(version_elements)
        attributes = {}
        ve_cnt = len(version_elements)
        for i in range(ve_cnt):
            version_element = version_elements[i]
            print("THis is inside for loop")
            version_element.click()
            version_elements = driver.find_elements(By.CSS_SELECTOR, "#main_body .player_versions > li > a")
            print("This is after lcick version element")
            player_stats_element = driver.find_elements(By.ID, "player_stats")
            print(player_stats_element)
            if player_stats_element is None or len(player_stats_element) == 0:
                continue
            columns = driver.find_elements(By.CSS_SELECTOR, "#player_stats .column")
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
                    attributes[name][td_elements[0].text.strip()] = td_elements[1].text.strip()
            break

        print(attributes)
        with open("player_stats.json", "w") as f:
            json.dump(attributes, f, indent=4)
    except Exception as e:
        print(str(e))
get_attributes_from_fminside(driver)


