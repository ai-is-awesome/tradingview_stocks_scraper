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

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    return webdriver.Chrome(options = options)
    

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
        driver = webdriver.Chrome(options = options)
    
    
        
    scraper = TradingViewScraper(url, driver)
#    driver.close()
    return scraper.get_all_details()

