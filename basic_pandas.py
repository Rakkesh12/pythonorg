import pandas as pd
import numpy as np
"""list_1=[111,222,78]
b=pd.Series(list_1,index=['rakkesh','sai','manoj'],dtype='float64')
print(b[0])
print(b['rakkesh'])
print(b)"""

"""my_details={'bike':['r15','pulsar','ns200'],'price':[400000,250000,34678]}
s_1=pd.DataFrame(my_details)
print(s_1.loc[[0,1]])
print(s_1)
print(pd.__version__)"""


"""data_1=pd.read_csv('rakesh.txt')
print(data_1.head(2))
print(data_1.info())
print(data_1)"""

#date=pd.date_range(start='20011601',end='20012601',periods=6,freq=1)
#print(date)

dates=pd.date_range(20130101,20130124,periods=4)
#print(dates)
#a_1={'bike':['r15','pulsar','ns200','ninja'],'price':[400000,250000,34678,10000000]}
#data_frame=pd.DataFrame(a_1,index=dates)
data_frame=pd.DataFrame(np.random.randn(4,3),index=dates,columns=range(10,40,10))
print(data_frame)


"""data_frame_2=pd.DataFrame(
    {
        'a':10,
        'b':'raki',
        'c':pd.Series(1,range(4)),
        'd':np.array([3]*4,dtype='int32')
    }
)
print(data_frame_2)
#print(data_frame_2.index)
#print(data_frame_2.columns)
#print(data_frame_2.describe())
#print(data_frame_2.to_numpy())
#print(data_frame_2.T)
print(data_frame_2.sort_index())"""


