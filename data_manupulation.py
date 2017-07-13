import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ochl
import matplotlib.dates as mdates
style.use('ggplot')
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2017, 6, 6)

# ticker = "TSLA"
# df = web.DataReader(ticker.strip('\n'), "google ", start, end)
# df = web.DataReader('TSLA', 'google', start, end)
# print(df.head(10))
# print(df.tail(10))
# df.to_csv('tsla.csv')


#simple Plotting data using matplotlib
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)


# Resampling the data
# Open High low close graph over 10day
df_ohlc = df['High'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

print(df_ohlc.head())
# print(df_volume)

# make date as column
df_ohlc.reset_index(inplace=True)
print(df_ohlc.head())

# make date column as mdate
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
print(df_ohlc.head())

# Share X makthe both axis share the axis so zoom in make easy
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.xaxis_date()

candlestick_ochl(ax1, df_ohlc.values, width=2, colorup='g', colordown='k', alpha=0.75)
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)



plt.show()
