#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Used for data analytics library 


# In[3]:


#command to install pandas

get_ipython().system('pip install pandas')


# In[ ]:


#understanding the datastructure of pandas

#1. series
#2, Dataframes
#3, Panel

#all the datastructure is build on numpy thus performance is very fast for pandas they are written over numpy


# In[ ]:


#series= 1D,singular format|homogenous array

#Dataframes= 2 D homogenous array |tabular format

#Panel = 3D array , asteroids metroids 3D concepts it is used


# In[ ]:


#what kind of data types pandas consists of??
#Ans: All pandas datastructure are immutable except series datatype which is mutable


# In[23]:


import numpy as np
import pandas as pd

#Pandas Series:

#basic syntax -- pandas.series(data,index,dtype,copy)

x = pd.Series()
print(x)

#Interview Questions : #As pandas is built on NUMPY thus its default datatype is also float


# In[28]:


import numpy as np
import pandas as pd
data = np.array(['a','b','c','d','e'])
j = pd.Series(data)
print(j)


# In[27]:


#how to get the customised indexing?? keep index -101,102,103,104,105 by default it is 0 1 2 3 4

data = np.array(['a','b','c','d','e'])
s = pd.Series(data,index=[101,102,103,104,105])
print(s)


# In[ ]:




