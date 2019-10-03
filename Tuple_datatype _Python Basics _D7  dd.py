#!/usr/bin/env python
# coding: utf-8

# In[1]:


#immutable list is called tuple
#how to define a tuple
x = (1,2,3,4)
print(x)


# In[4]:


dimensions = (200,50)
#how to choose elements in a tuple
print(dimensions[0])
print(dimensions[1])


# In[5]:


#zen of python
import this


# In[11]:


my_food = ['piz','past','paneer','aalu','laalu']
friends_food =  my_food                                                                  
print(friends_food)


friends_food.append('Tree')
print(friends_food)


# In[ ]:


PEP -8

python enhancement prapolas -8:
    CODE CONSISTENCY:


# In[13]:


#implementation of if condition

#validationg a condition
#1) maruti comes up,all letters need to be capatalize
#2) any other car comes up it needs to be formatted in a title case
cars = ['audi','bmw','benz','maruti']

for car in cars:
    if car == 'maruti':
        print(car.upper())
    else:
        print(car.title())
    


# In[ ]:




