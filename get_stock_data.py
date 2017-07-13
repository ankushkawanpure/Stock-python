# Get data from google finance and store as csv

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2017, 6, 2)

# ticker = "TSLA"
# df = web.DataReader(ticker.strip('\n'), "google ", start, end)

df = web.DataReader('TSLA', 'google', start, end)
# print(df.head(10))
# print(df.tail(10))
df.to_csv('tsla.csv')

