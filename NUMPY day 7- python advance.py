#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#splitting operations in array
X = NP.ARANGE(9)


# In[3]:


X = np.ARANGE(9)


# In[4]:


X = np.arange(9)


# In[5]:


#we need to only use num which is divisible by the no. of elements in an array
X


# In[6]:


print('split the array into 3 equal sized subarrays')
np.split(X,3)


# In[7]:


print('split the array at positions indicated  in 1-d array:')
np.split(X,[4,7])


# In[8]:


np.split(X,[5,7])


# In[9]:


y=np.array([('germany','france','hungary','austria'),
           ('berlin','paris','budapest''vuenna')])


# In[11]:


p1,p2 =np.hsplit(y,2)  #axis = 0 that is cut in the column level


# In[12]:


print(p1)


# In[13]:


print(p2)


# In[22]:


y=np.array([('germany','france','hungary','austria'),
           ('berlin','paris','budapest','vuenna')])

y


# In[17]:


print(p1)


# In[23]:


p1,p2 =np.hsplit(y,2)

print(p1)
print(p2)


# In[18]:


print(p2)


# In[19]:


q1,q2 = np.vsplit(y,2)  #axis = 1 that is cut in the Row level


# In[20]:


print(q1)


# In[21]:


print(q2)


# In[ ]:




