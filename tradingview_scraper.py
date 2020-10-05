# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:35:26 2020

@author: Piyush
"""

from bs4 import BeautifulSoup

from requests_module import Request
import selenium
from selenium import webdriver
from config import CHROME_PATH
from utils import get_text_or_none
import traceback




    


def is_relevant_speedo(speedo_div):
    for span in speedo_div.find_all('span'):
        if span.attrs.get('class') and 'speedometerTitle' in span.attrs.get('class')[0]:
            return True
    for h3 in speedo_div.find_all('h3'):
        if h3.attrs.get('class') and 'speedometerTitle' in h3.attrs.get('class')[0]:
            return True
    
    return False
    


class TradingViewScraper:
    def __init__(self, url_or_ticker_name, driver):
        try:
            self.driver = driver
        except:
            self.driver = webdriver.Chrome(CHROME_PATH)
        self.url_or_ticker_name = url_or_ticker_name
        
        self.soup = self.get_soup()
        
    def get_soup(self, ):
        self.driver.get(self.url_or_ticker_name)
        text = self.driver.page_source
        soup = BeautifulSoup(text, 'lxml')
        return soup
    
    def get_speedometer_details(self, speedometer_div):
        title = speedometer_div.select_one("*[class*='speedometerTitle']")
        title = title.text if title else title
        signal = speedometer_div.select_one("*[class*='speedometerSignal']").text
        bottom_wrapper = speedometer_div.select_one("*[class*='countersWrapper']")
        bottom_wrapper_list = list()
        for counter in bottom_wrapper:
            counter_title= counter.select_one("*[class*='counterTitle']").text
            number = counter.select_one("*[class*='counterNumber']").text
            bottom_wrapper_list.append({counter_title: number})
    
        return {'speedometer_title' : title, 'speedometer_signal' : signal, 'speedometer_counters' : bottom_wrapper_list}
    
    def get_all_speedometers(self, soup):
        try:
            speedometer_container = soup.select_one("div[class*='speedometersContainer']")
            speedometer_divs = speedometer_container.select("div[class*='speedometerWrapper']")
            relevant_speedometer_divs = [speedometer_div for speedometer_div in speedometer_divs if is_relevant_speedo(speedometer_div)]
            L = [self.get_speedometer_details(relevant_speedometer_div) for relevant_speedometer_div in relevant_speedometer_divs]
        except:
            print('No speedometers found!')
            L = list()
        return L
    
    def scrape_table(self, table_container):
        table =table_container.find('table')
        title = table_container.select('div[class*="title"]')[0].text
        header = table.select_one("tr[class*='header']")
        columns = [h.text for h in header.find_all('th')]
        rows = table.select("tr[class*='row']")
        table_dict = {key: list() for key in columns}
        for row in rows:
            row_data = row.select("td[class*='cell']")
            for cell_data, i in zip(row_data, range(len(row_data))):
                table_dict[columns[i]].append(cell_data.text)
            
        return_dict = {'table_title' : title, 'table_columns' : columns, 'table_content' : table_dict}
        return return_dict
    
    
    
    def get_all_tables(self, soup):
        tables_container = soup.find_all('div', class_ = 'container-2w8ThMcC')
        L  = [self.scrape_table(table) for table in tables_container]
        return L
    
    
    def get_stock_details(self, soup):
        
        short_title = soup.find('div', class_  = 'tv-symbol-header__short-title')
        
        long_title = soup.find('div', class_ = 'tv-symbol-header__long-title-first-text')
        changes =soup.select("div.tv-symbol-price-quote__row > div.js-symbol-change-direction")
        
        try:
            changes_dict = {}
            spans = changes[0].find_all('span')
            for span, i in zip(spans, range(len(spans))):
                changes_dict['change_%s' % (i+1)] = span.text
                
        except:
            traceback.print_exc()
            changes_dict = {}
        
        header = soup.find('div' , class_ = 'tv-category-header__fundamentals')        
        
        def get_block_information():
            blocks = header.find_all('div', class_ = 'tv-fundamental-block')
            blocks_list = list()
            
            for block in blocks:
                try:
                    value = block.find('div', class_ = 'tv-fundamental-block__value').text
                    title = block.find('div', class_ = 'tv-fundamental-block__title').text
                    if title and value:
                        blocks_list.append({title: value})
                except:
                    pass
                
            return blocks_list
        
        return_D = {'short_title' : get_text_or_none(short_title).strip('\n') if short_title else None, 
         'long_title' : get_text_or_none(long_title), 
         'other_information' : get_block_information()
         
         }
            
        return_D.update(changes_dict)
        
        
        return return_D
        
    def get_all_details(self):
        soup = self.soup
        speedometers = self.get_all_speedometers(soup)
        tables = self.get_all_tables(soup)
        stock_details = self.get_stock_details(soup)
        D = {'speedometers' : speedometers, 
             'tables' : tables, 
             'stock_details' : stock_details}
        
        return D
    
    


    
test_url= 'https://www.tradingview.com/symbols/NASDAQ-AAPL/technicals/'



