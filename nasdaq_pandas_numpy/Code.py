import pandas as pd
import numpy as np

# importing data
ndata=np.genfromtxt('nasdaq.csv', delimiter=',',dtype=None, names=True, case_sensitive=True)
# Condition for data
#data_mean=ndata['Volume'].mean()
#data_median=np.median(ndata['Close'],axis=0)
#nfilter_data=ndata[(ndata['Volume']> data_mean) & (ndata['Close']> data_median) ]
## merging condition
ntemp_filter=np.vstack((ndata['Low'],ndata['High']))
 #create new condition
nnew_data=np.add(ndata['Low'],ndata['High'])/2
nfinal=(np.vstack((ntemp_filter,nnew_data))).T
# merging All
nnew_final=pd.DataFrame({'Low': nfinal[:, 0], 'High': nfinal[:, 1], 'Average':nfinal[:,2]})
# saving in CSV file
pd.DataFrame(nnew_final).to_csv("nfinal.csv")

ndata=np.genfromtxt('nfinal.csv', delimiter=',',dtype=None, names=True, case_sensitive=True)

print(ndata['Average'])

