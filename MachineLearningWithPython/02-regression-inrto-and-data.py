
# ml  regression - intro and data
import pandas as pd 
import quandl

import xml.etree.ElementTree as elemTree

tree = elemTree.parse('quandl.xml')
root = tree.getroot()
quandl.ApiConfig.api_key = root.find('./key').text


df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume', ]]

df['HL_PCT'] = ((df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'])*100.0
df['PCT_change'] = ((df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'])*100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume', ]]

print(df)