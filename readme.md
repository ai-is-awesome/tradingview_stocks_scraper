# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 07:39:50 2020

@author: Piyush
"""

<h1>
TradingView Scraper
</h1>

<h3> This bot uses Selenium to make the get requests then passes the html file to the scraper which then scrapes all the data.<br>
The scraper then returns the results in a json like format of list, with each element of list being a dictionary. 


</h3>

<h2>Setting up the repo
</h2>
  
  <h3>Make sure you've installed everything from requirements.txt
  
  <ul>
  <li>
  To install, use a virtual environment and open the project directory in cmd and use<br>
 </li>
  <li>
  pip install -r requirements.txt
  </li>
  <li>
  After that, go to 'C:\Program Files (x86)\chromedriver.exe' and paste the chrome driver to setup the selenium driver
  </li>
  </h3>

<h2 style =  "text-align: center;">
How to use the bot
</h2>

<h3>
<ul>
<li>To use the bot, open the config.py file
</li>
<li>Assign the value of CHROME_PATH to the path of your selenium chrome web driver.</li>


<li>
Now, go to the main.py file and run the module. 
Example URL: 'https://www.tradingview.com/symbols/NASDAQ-AAPL/technicals/'

</li>
<li>
To run the scraper on above url, call the function main with the above url and the driver instance. 
main('https://www.tradingview.com/symbols/NASDAQ-AAPL/technicals/', driver)

</li>


<li>
The scraper should return a JSON like structure of list of dictionaries. 
</li>

