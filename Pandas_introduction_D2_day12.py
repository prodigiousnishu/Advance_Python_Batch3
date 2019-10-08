#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Constants & scaler

the fixed value:


# In[1]:


import pandas as pd
x = pd.Series(5, index =[0,1,2,3,4,5])
print(x)


# In[2]:


#how to access data from the series

#customised indexing
x = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])

print(x)


# In[3]:


print (x[0])


# In[5]:


print(x[0:3])


# In[6]:


#or
print (x[:3])


# In[7]:


print(x[-1:-4])


# In[8]:


#last 3 elements
print(x[-3:])


# In[9]:


#using customised indexing find the 2nd element
print(x['b'])


# In[ ]:




