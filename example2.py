import pandas as pd
import numpy as np

# importing data
ndata=np.genfromtxt('nasdaq.csv', delimiter=',',dtype=None, names=True, case_sensitive=True)
# Condition for data
data_mean=ndata['Volume'].mean()
data_median=np.median(ndata['Close'],axis=0)
nfilter_data=ndata[(ndata['Volume']> data_mean) & (ndata['Close']> data_median) ]
# merging condition
ntemp_filter=np.vstack((nfilter_data['Open'],nfilter_data['Close']))
# create new condition
nnew_data=np.add(nfilter_data['Open'],nfilter_data['Close'])/2
nfinal=(np.vstack((ntemp_filter,nnew_data))).T
# merging All
nnew_final=pd.DataFrame({'Open': nfinal[:, 0], 'Close': nfinal[:, 1], 'Mid':nfinal[:,2]})
# saving in CSV file
pd.DataFrame(nnew_final).to_csv("nfinal.csv")

