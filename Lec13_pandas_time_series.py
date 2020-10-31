
# # Time Series

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ## Date and Time Data Types and Tools

from dateutil.parser import parse
parse('2011-01-03')
parse('Jan 31, 1997 10:45 PM')
parse('6/12/2011', dayfirst=True)
parse('6/12/2011')


#%%
datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
pd.to_datetime(datestrs)

idx = pd.to_datetime(datestrs + [None])
idx
idx[2]
pd.isnull(idx)

# ## Time Series Basics
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4),
                       index=dates,
                       columns=['Colorado', 'Texas',
                                'New York', 'Ohio'])
long_df.loc['5-2001']


# ## Date Ranges, Frequencies, and Shifting
resampler = long_df.resample('D')


# ### Generating Date Ranges
#%%
index = pd.date_range('2012-04-01', '2012-06-01')
index

pd.date_range(start='2012-04-01', periods=20)
pd.date_range(end='2012-06-01', periods=20)

# ### Frequencies and Date Offsets
#%%
pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4h')
pd.date_range('2000-01-01', periods=10, freq='1h30min')


# #### Week of month dates
rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')
list(rng)


# ### Shifting (Leading and Lagging) Data

#%%
ts = pd.Series(np.random.randn(4),
               index=pd.date_range('1/1/2000', periods=4, freq='M'))
ts
ts.shift(2)
ts.shift(-2)



# ## Periods and Period Arithmetic

#%%
p = pd.Period(2007, freq='A-DEC')
p

rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
rng

pd.Series(np.random.randn(6), index=rng)

values = ['2001Q3', '2002Q2', '2003Q1']
index = pd.PeriodIndex(values, freq='Q-DEC')
index



# ### Converting Timestamps to Periods (and Back)
rng = pd.date_range('2000-01-01', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)
ts
pts = ts.to_period()
pts

rng = pd.date_range('1/29/2000', periods=6, freq='D')
ts2 = pd.Series(np.random.randn(6), index=rng)
ts2
ts2.to_period('M')



# ### Creating a PeriodIndex from Arrays
#%%
data = pd.read_csv('examples/macrodata.csv')
data.head(5)
data.year
data.quarter


index = pd.PeriodIndex(year=data.year, quarter=data.quarter,
                       freq='Q-DEC')
index
data.index = index
data.infl


# ## Resampling and Frequency Conversion
#%%
rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ts.resample('M').mean()
ts.resample('M', kind='period').mean()


# ### Downsampling

rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.arange(12), index=rng)
ts

ts.resample('5min', closed='left').sum()
ts.resample('5min', closed='right').sum()

ts.resample('5min', closed='right', label='right').sum()
ts.resample('5min', closed='right',
            label='right', loffset='-1s').sum()


# #### Open-High-Low-Close (OHLC) resampling
#%%
ts.resample('5min').ohlc()


# ### Upsampling and Interpolation
#%%
frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
frame


df_daily = frame.resample('D').asfreq()
df_daily

frame.resample('D').ffill()
frame.resample('D').ffill(limit=2)
frame.resample('W-THU').ffill()


# ### Resampling with Periods
frame = pd.DataFrame(np.random.randn(24, 4),
                     index=pd.period_range('1-2000', '12-2001', freq='M'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
frame[:5]
annual_frame = frame.resample('A-DEC').mean()
annual_frame


# Q-DEC: Quarterly, year ending in December
annual_frame.resample('Q-DEC').ffill()


# ## Moving Window Functions
#%%
close_px_all = pd.read_csv('examples/stock_px_2.csv',
                           parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()

close_px.AAPL.plot()
close_px.AAPL.rolling(250).mean().plot()

appl_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
appl_std250
appl_std250.plot()
close_px.rolling('20D').mean()


aapl_px = close_px.AAPL['2006':'2007']
ma60 = aapl_px.rolling(30, min_periods=20).mean()
ewma60 = aapl_px.ewm(alpha=0.1).mean()
aapl_px.plot()
ma60.plot(style='k--', label='Simple MA')
ewma60.plot(style='k-', label='EW MA')
plt.legend()


# ### Binary Moving Window Functions
#%%
spx_px = close_px_all['SPX']
spx_rets = spx_px.pct_change()
returns = close_px.pct_change()

corr = returns.AAPL.rolling(125, min_periods=100).corr(spx_rets)
corr

corr = returns.rolling(125, min_periods=100).corr(spx_rets)
corr.plot()
corr

# ### User-Defined Moving Window Functions
#%%
from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
result.plot()
