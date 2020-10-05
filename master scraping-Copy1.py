#!/usr/bin/env python
# coding: utf-8

# In[37]:


from bs4 import BeautifulSoup

from requests_module import Request


# In[39]:


from save_soup import save_soup


# In[40]:


import selenium


# In[41]:


from selenium import webdriver


# In[42]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs


# In[43]:


path = 'C:/Program Files (x86)/chromeDriver.exe'


# In[44]:


driver = webdriver.Chrome(path)


# In[45]:


url = 'https://www.tradingview.com/symbols/NASDAQ-AAPL/technicals/'


# In[46]:


driver.get(url)


# In[47]:


src = driver.page_source


# In[48]:


s = bs(src, 'lxml')


# # Trash

# In[17]:


s.find('span', class_ = 'counterNumber-3l14ys0C sellColor-2qa8ZOVt')


# In[21]:


driver.find_element_by_class_name('tab-1Yr0rq0J').click()


# In[ ]:


'tab-1Yr0rq0J'


# In[22]:


'tab-B2mArR2X tab-1Yr0rq0J noBorder-oc3HwerO' == 'tab-B2mArR2X tab-1Yr0rq0J noBorder-oc3HwerO'


# In[23]:


'tab-B2mArR2X tab-1Yr0rq0J noBorder-oc3HwerO' == 'tab-B2mArR2X tab-1Yr0rq0J noBorder-oc3HwerO'


# In[ ]:


'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'


# In[37]:


driver.find_element_by_class_name('RY3tic').click()


# In[42]:


driver.find_element_by_class_name('VfPpkd-kBDsod')


# In[32]:


driver.current_url


# In[17]:


r = Request.get(url)


# In[ ]:


s = bs(r.text, 'lxml')


# 

# # getting soup

# In[49]:


soup = bs(driver.page_source, 'lxml')


# # scraping speedometers

# ## speedometer container -> speedometer wrapper 

# In[50]:


for div in soup.find_all('div'):
    if div.attrs.get('class') and 'speedometersContainer' in div.attrs.get('class')[0]:
        speedometer_container = div


# In[51]:


speedometer_divs = list()
for div in speedometer_container.find_all('div'):
    if div.attrs.get('class') and 'speedometerWrapper' in div.attrs.get('class')[0]:
        speedometer_divs.append(div)
        for span in div.find_all('span'):
            if span.attrs.get('class') and 'speedometerTitle' in  span.attrs.get('class')[0]:
#                 print(span)
                pass


# In[52]:


def is_relevant_speedo(speedo_div):
    for span in speedo_div.find_all('span'):
        if span.attrs.get('class') and 'speedometerTitle' in span.attrs.get('class')[0]:
            return True
    for h3 in speedo_div.find_all('h3'):
        if h3.attrs.get('class') and 'speedometerTitle' in h3.attrs.get('class')[0]:
            return True
    
    return False
    


# In[53]:


len(list(filter(is_relevant_speedo, speedometer_divs)))


# In[54]:


relevant_speedos = [speedometer_div for speedometer_div in speedometer_divs if is_relevant_speedo(speedometer_div)]


# In[55]:


relevant_speedos = list(filter(is_relevant_speedo, speedometer_divs))


# In[56]:


for speedo_div in speedometer_divs:
    print(is_relevant_speedo(speedo_div))


# In[57]:


# If it's a wrappper we don't want that!
speedometer_divs[1].next_element


# # getting title of speedo

# In[58]:


# Look for the elements h3 and span


# In[59]:


temp = ['h3', 'span']


# # amazing!

# In[60]:


speedometer_divs[0].select("*[class*='speedometerTitle']")


# In[61]:


for ele_name in temp:
    for tag in speedometer_divs[0].find_all(ele_name):
        if tag.get('class') and 'speedometerTitle' in tag.get('class')[0]:
            print(tag.text)


# # signal of speedo

# In[62]:


for span in speedometer_divs[0].find_all('span'):
#     print(span)
    if span.get('class') and 'speedometerSignal' in span.get('class')[0]:
        print(span.text)


# # getting bottom wrapper

# In[67]:


'countersWrapper'
for div in speedometer_divs[0].find_all('div'):
    if div.attrs.get('class') and 'countersWrapper' in div.attrs.get('class')[0]:
        bottom_wrapper = div


# In[68]:


for div in bottom_wrapper.find_all('div'):
    if 'counterWrapper' in div.attrs.get('class')[0]:
        counter = div
        num = counter.find_next('span').text
        title = counter.find_next('span').find_next('span').text
        print(title, num)
        


# In[72]:


temp = bottom_wrapper.select("div[class*='counterWrapper']")[0]


# In[75]:


temp.select_one("*[class*='counterTitle']")


# In[76]:


temp.select_one()


# In[95]:


def get_speedometer_details(speedometer_div):
    title = speedometer_div.select_one("*[class*='speedometerTitle']")
    title = title.text if title else title
    print(title)
    signal = speedometer_div.select_one("*[class*='speedometerSignal']").text
    bottom_wrapper = speedometer_div.select_one("*[class*='countersWrapper']")
    bottom_wrapper_list = list()
    for counter in bottom_wrapper:
        counter_title= counter.select_one("*[class*='counterTitle']").text
        number = counter.select_one("*[class*='counterNumber']").text
        bottom_wrapper_list.append({counter_title: number})
    
    return {'speedometer_title' : title, 'speedometer_signal' : signal, 'speedometer_counters' : bottom_wrapper_list}
    


# In[94]:


get_speedometer_details(speedometer_divs[0])


# # Now iterate and do it for all the speedos

# # scraping table

# In[86]:


def class_contains_text(div):
    pass


# In[ ]:


soup.find_all('div')


# In[89]:


f = lambda div, keyword : div.attrs.get('class') and keyword in div.attrs.get('class')[0]


# In[101]:


for div in soup.find_all('div'):
    if f(div, 'tablesWrapper'):
        tables = div


# # this doesn't work for the pivots table

# In[260]:


tables_container = tables.select('div[class*="container"]')


# In[276]:


tables_container = soup.find_all('div', class_ = 'container-2w8ThMcC')


# In[168]:


table_container = tables_container[0]


# # title

# In[174]:


table_container.select('div[class*="title"]')[0].text


# In[177]:


table =table_container.find('table')


# # getting table columns

# In[183]:


header = table.select_one("tr[class*='header']")


# In[186]:


columns = [h.text for h in header.find_all('th')]
columns


# # finding rows of data

# In[217]:


table_dict = {key: list() for key in columns}


# In[218]:


rows = table.select("tr[class*='row']")


# # Cell that does it All!

# In[219]:


for row in rows:
    row_data = row.select("td[class*='cell']")
    for cell_data, i in zip(row_data, range(len(row_data))):
        table_dict[columns[i]].append(cell_data.text)
        


# In[223]:


tables_container[1]


# In[234]:


def scrape_table(table_container):
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


# In[242]:


# L = list()
[scrape_table(table_container) for table_container in tables_container][1]


# In[259]:


soup.find_all('div', class_ ='container-2w8ThMcC')[2].select("div[class*='title']")


# In[268]:


for a in soup.find_all('a'):
    if a.attrs.get('href') == '/ideas/pivotpoints/':
        temp = a


# In[271]:


temp.parent.parent


# In[275]:


soup.select("div[class*='container']")


# In[ ]:




