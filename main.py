# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:40:44 2020

@author: Piyush
"""
from tradingview_scraper import TradingViewScraper
from utils import url_formatter
from selenium import webdriver
import exceptions
from selenium.webdriver.chrome.options import Options
from config import CHROME_PATH

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    if CHROME_PATH == '':
        return webdriver.Chrome(options = options)
    else:
        return webdriver.Chrome(CHROME_PATH, options = options)
    

#delete this if module needs to be loaded over and over again!
driver = get_driver()

def main(url_or_tickername, driver = None):
    if url_or_tickername.startswith('http') or url_or_tickername.startswith('www.'):
        is_url = True
    else:
        is_url = False
        
    
    if is_url:
        url = url_or_tickername
        
    else:
        url = url_formatter(url_or_tickername)
        
    if not driver:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        if CHROME_PATH == '':    
            driver = webdriver.Chrome(options = options)
        else:
            driver = webdriver.Chrome(CHROME_PATH, options = options)
    
    
        
    scraper = TradingViewScraper(url, driver)
#    driver.close()
    return scraper.get_all_details()



def close_driver(driver):
    driver.close()


test_url= 'https://www.tradingview.com/symbols/NASDAQ-AAPL/technicals/'