from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from dotenv import load_dotenv

from FMInsideFetch import FMInsideFetch
from EASportsFetch import EASportsFetch
from FutBinFetch import FutBinFetch
load_dotenv()




class PlayerRatingFetch:
    def __init__(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-gpu')
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(100)
    """
    fetch player data from fminside
    """
    def fetch_player_data_from_fminside(self, player_name):
        url = os.getenv("FMINSIDE_URL")
        fminside_fetch = FMInsideFetch(self.driver, player_name, url)
        player = fminside_fetch.do_fetch()
        print(player)

    def fetch_player_data_from_sofascore(self):
        url = os.getenv('SOFASCORE_URL')
        futbin_fetch = FutBinFetch(self.driver, player_name, url)
        player = futbin_fetch.do_fetch()
        print(player)
        
    def fetch_player_data_from_futbin(self):
        url = os.getenv('FUTBIN_URL')

        
    def fetch_player_data_from_ea(self, player_name):
        url = os.getenv('EA_SPORTS_FC_URL')
        ea_sports_fetch = EASportsFetch(self.driver, player_name, url)
        player = ea_sports_fetch.do_fetch()
        print(player)
        
    def fetch_player_data_from_football_lineups(self):
        url = os.getenv('FOOTBALL_LINEUPS_URL')
        