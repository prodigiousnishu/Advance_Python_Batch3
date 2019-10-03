#!/usr/bin/env python
# coding: utf-8

# In[31]:


#iterating
import numpy as np

#1d arrau
a = np.arange(11)**2
a


# In[32]:


#multidimensional array
students = np.array([['amit','teja','anil','veena'],[65,78,90.81,85],[71,82,79,92,95]])
students


# In[33]:


for s in students:
    print('marks=',s)


# In[19]:


for element in students.flatten():
    print(element)
    #what is flattening order- row wise (C order)


# In[20]:


#column order --- > known as forton order
for element in students.flatten(order='F'):
    print(element)
    


# In[21]:


#nditer
#efficient multimensional iterator object to iterate over arrays
x= np.arange(12).reshape(3,4)
x


# In[7]:


for i in np.nditer(x):
    print(i) #rowise iteration nditer


# In[30]:


#column wise
for i in np.nditer(x, order= 'F'):
    print(i)


# In[23]:


#flag concept

for i in np.nditer(x, order = 'F',flags = ['external_loop']):
    print(i)


# In[ ]:




