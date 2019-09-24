#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x= np.array([1,2,3])
x


# In[4]:


y= np.array([(1,2,3),(4,5,6)])
y


# In[5]:


y.shape


# In[6]:


type(y) 


# In[7]:


num=[1,2,3,4]
np.array(num)


# In[9]:


#built in functions to create array as per our requirement

#array of zeros

x=np.zeros((3,3))
x


# In[11]:


#Arrays of ones

x=np.ones((3,3))
x


# In[13]:


#Default datatype is float but we can change it in the defination as below

#how to change the datatype

x=np.ones((3,3),dtype=np.int16)
x


# In[15]:


#empty array
array_empty = np.empty((2,3))
array_empty


# In[16]:


#identity MAtrix generation
array_eye = np.eye((3))
array_eye


# In[18]:



x=np.two((3,3),dtype=np.int16)
x


# In[ ]:





# In[20]:


#python = range(x,y)
#numpy = arange(start,stop,step count,datatype)
array_of_event = np.arange(2,20,2,int)
array_of_event 


# In[22]:



x=np.ones((3,3),dtype=np.int16)
x


# In[23]:



x=np.ones((3,3),dtype=np.int16)
x*2**2


# In[ ]:




