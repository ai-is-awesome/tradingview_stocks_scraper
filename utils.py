# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 01:37:47 2020

@author: Piyush
"""



def get_text_or_none(tagOrNone):
    if not tagOrNone:
        return None
    
    else:
        try:
            return tagOrNone.text
        
        except:
            return tagOrNone
    
    

def url_formatter(ticker):
    base_url = 'https://www.tradingview.com/symbols/%s/technicals/'
    return base_url % (ticker)