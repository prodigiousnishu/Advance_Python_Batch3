#!/usr/bin/env python
# coding: utf-8

# # Arithmetic Operations

# In[1]:


import numpy as np


# In[2]:


a = np.array([10,10,10])
b = np.array([5,5,5])


# In[3]:


a + b


# In[4]:


a - b


# In[5]:


a * b


# In[6]:


a / b

#when ever we are applying division the output datatype by default will be float..


# In[7]:


a % b 

# gives Reminder as o/p


# In[ ]:


# Prime No (divisable by 1 or itself)
# Factorial (5! = 5*4*3*2*1)
# Fabonacci Series
# Arm strong Series
# Palendrome


# In[8]:


a % 3


# In[9]:


a < 35


# In[10]:


a < 9


# In[ ]:


#why to use array in above exercise?

#Arrays are used due to high n fast performance than any other data type


# In[13]:


#Modifying array without creating any new one
import numpy as np
a += 3

a


# In[23]:


b =+a
b


# In[19]:


#Unary Operator

ages=np.array([12,15,18,20])

ages.sum()


# In[20]:


ages.min()


# In[21]:


ages.max()


# In[ ]:




