#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = ['dog','cat','fish','duck']


# In[2]:


#pop -- its a function which is used to delete a element from the last of a list
a.pop()


# In[3]:


a


# In[4]:


a.pop(0)


# In[5]:


a


# In[6]:


motorcycles = ['honda','yamaha','suzuki','ducati']
motorcycles


# In[7]:


motorcycles.remove('ducati')
print(motorcycles)


# In[10]:


cars = ['bmw','audi','toyota','benz']


# In[11]:


cars.sort()
print(cars)
# by using sort the lit will be sorted permanently and can not be rechanged


# In[12]:


cars


# In[13]:


cars_1 = ['maruti','tata','landrover','jaguar']

print('here is the original list:')

print(car_1)


# In[17]:


cars_y = ['maruti','tata','landrover','jaguar']

print('here is the original list:')

print(cars_y)

print('here is the sorted list:')

cars_y.sorted()

print(cars_y)


# In[ ]:


#IQ: what is the difference between sorted and sort

#sort will change the position of element permanently
#sort will change the position of element temporarily


# In[18]:


#IQ: how to reverse elemt in list

cars_1 = ['maruti','tata','landrover','jaguar']

cars_1.reverse()

print(cars_1)


# In[ ]:


cars_1 = ['maruti','tata','landrover','jaguar']

cars_1.count()

print(cars_1)

