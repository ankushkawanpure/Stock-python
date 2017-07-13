import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

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
print(df.head(10))
print(df.tail(10))

print(df[['Open', 'High']].head())
df['Close'].plot()
# plt.show()


# Calculate 100 day moving average
df['100ma'] = df['Close'].rolling(window=100).mean()
df.dropna(inplace=True)
print(df.tail(10))

# Plot of 100 day moving average with closing price with volume
# Share X make the both axis share the axis so zoom in make easy
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()