#!/usr/bin/env python
# coding: utf-8

# In[25]:


from bs4 import BeautifulSoup
import bs4
import urllib.request as ur
import requests
from lxml import html
import re
import pandas as pd
import numpy as np
import datetime as dt


# In[35]:


#Data Frame of Active Stocks
NASDAQ = pd.read_csv(r'D:\Portfolio Work\NASDAQ.csv')
AMEX = pd.read_csv(r'D:\Portfolio Work\AMEX.csv')
NYSE = pd.read_csv(r'D:\Portfolio Work\NYSE.csv')

#Markets
Markets = [NASDAQ, AMEX, NYSE]

#Creating a reference data frame to find the symbol when the input receives a name
name_industry = pd.concat(Markets, axis = 0)

#Drop unneeded columns
name_industry = name_industry.drop(columns = ['LastSale', 'MarketCap','IPOyear','Summary Quote'])
name_industry.drop(name_industry.columns[name_industry.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

#Fix some weird stuff in the csv
name_industry.Name.replace({'&#39;s':"'s"}, regex = True)


# In[36]:


#Create the matching DataFrame
match = pd.DataFrame(name_industry)

#Identify the match with the stock entered
match = match[match['Name'].str.match(input("Enter the name of a stock to add to the DB:"))]
print('These are our result(s):')
print(match)


# In[ ]:


#Make the stock searchable by entering the symbol
sym = input("Type the Symbol of which security you want:")

#Go to yahoo to pull financial statements
url = 'https://finance.yahoo.com/quote/' + sym + '/financials/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip , deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Pragma': 'no-cache',
    'Referrer': 'https://google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

page = requests.get(url, headers)

tree = html.fromstring(page.content)

tree.xpath("//h1/text()")


# In[ ]:


table_rows = tree.xpath("//div[contains(@class, 'D(tbr)')]")

#Ensure table rows are found, if none are found it's possiblke that either the layout of the page has been changed 
#or my scraper attempts have been detected and THWARTED

assert len(table_rows) > 0

parsed_rows = []

for table_row in table_rows:
    parsed_row = []
    el = table_row.xpath("./div")
    
    none_count = 0
    
    for rs in el:
        try:
            (text,) = rs.xpath('.//span/text()[1]')
            parsed_row.append(text)
        except ValueError:
            parsed_row.append(np.NaN)
            none_count += 1
            
    if (none_count < 4):
        parsed_rows.append(parsed_row)
        
df = pd.DataFrame(parsed_rows)

#Export csv
df.to_csv('D:/Portfolio Work/Exported csv ALGO/' + sym + '.csv', encoding = 'utf-8') #set your own location


# In[ ]:


#find the opens, closes, highs, lows, 


# In[ ]:


def parsePrice(sym):
    r = requests.get('https://finance.yahoo.com/quote/'+ sym + '?p='+ sym)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text 
    return price


# In[ ]:


r = requests.get('https://finance.yahoo.com/quote/'+ sym + '?p='+ sym)
soup = bs4.BeautifulSoup(r.text, "lxml")


# In[ ]:


index_table = soup.find_all("table", attrs = {'class': 'W(100%)'})
index_table

index_table_data = []
for i in range(len(index_table)):
    index_table_data.append(index_table[i].tbody.find_all('td'))

headers = []
Values = []

for i in range(len(index_table)):
    for j in range(16):
        if j%2:
            Values.append(index_table[i].find_all('td')[j].string)
        else:
            headers.append(index_table[i].find_all('td')[j].string)
            
dictionary = {'Headers': headers, 'Values': Values}
most_recentdf = pd.DataFrame(data = dictionary)
most_recentdf = most_recentdf.drop([2,3])
most_recentdf.reset_index(inplace = True, drop = True)
most_recentdf.to_csv('D:/Portfolio Work/Exported csv ALGO/' + sym + 'Daily.csv', encoding = 'utf-8') #set your own location

