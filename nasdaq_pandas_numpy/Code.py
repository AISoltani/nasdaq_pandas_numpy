import pandas as pd
import numpy as np

# importing data
ndata=np.genfromtxt('nasdaq.csv', delimiter=',',dtype=None, names=True, case_sensitive=True)

def filter_by_close_std(data):
    close_mean = data['Close'].mean()
    close_std = data['Close'].std()
    filter_data = data[(data['Close'] > close_mean - close_std) & (data['Close'] < close_mean + close_std)]
    return filter_data

def add_returns_column(data):
    returns = np.diff(data['Close']) / data['Close'][:-1]
    returns = np.insert(returns, 0, 0)
    data['Return'] = returns
    return data

def rolling_average(data, window):
    rolling_avg = data['Close'].rolling(window=window).mean()
    return rolling_avg

def sharpe_ratio(data):
    returns = data['Return']
    risk_free_rate = 0.02 # assuming a 2% risk-free rate
    excess_returns = returns - risk_free_rate
    mean_excess_returns = excess_returns.mean()
    std_excess_returns = excess_returns.std()
    sharpe = mean_excess_returns / std_excess_returns
    return sharpe

# Condition for data
data_mean=ndata['Volume'].mean()
data_median=np.median(ndata['Close'],axis=0)
nfilter_data=ndata[(ndata['Volume']> data_mean) & (ndata['Close']> data_median) ]

# filter by close standard deviation
nfilter_data = filter_by_close_std(nfilter_data)

# add returns column
nfilter_data = add_returns_column(nfilter_data)

# calculate rolling average
rolling_avg = rolling_average(nfilter_data, 30)

# calculate Sharpe ratio
sharpe = sharpe_ratio(nfilter_data)

## merging condition
ntemp_filter=np.vstack((nfilter_data['Low'],nfilter_data['High']))
# create new condition
nnew_data=np.add(nfilter_data['Low'],nfilter_data['High'])/2
nfinal=(np.vstack((ntemp_filter,nnew_data))).T

# merging All
nnew_final=pd.DataFrame({'Low': nfinal[:, 0], 'High': nfinal[:, 1], 'Average':nfinal[:,2], 'Return':nfilter_data['Return']})
# saving in CSV file
pd.DataFrame(nnew_final).to_csv("nfinal.csv")

ndata=np.genfromtxt('nfinal.csv', delimiter=',',dtype=None, names=True, case_sensitive=True)

print(ndata['Average'])
print("Rolling Average:", rolling_avg)
print("Sharpe Ratio:", sharpe)