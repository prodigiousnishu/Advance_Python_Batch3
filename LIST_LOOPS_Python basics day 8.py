#!/usr/bin/env python
# coding: utf-8

# In[1]:


# for loop
students = ['nishant','surbhi','bhaiyu','pooja','ajinkya']
print(students)


# In[2]:


#x is a temp variable which takes the value by value from students and orints vertically
# : at the end
for x in students:
    print(x)


# In[9]:


for x in students:
    print(f"{x.title()},you are doing good")
    print(f"i will be looking for your assignment for today, {x.title()}.\n")
print("Thanks everyone for showing interest in using python")    


# In[11]:


#for making numerical list
for value in range(1,100):
    print(value)


# In[12]:


numbers = list(range(1,21))
print(numbers)


# In[14]:


#real nubers from 1-30
#range(start,stop,step)
even_num = list(range(2,31,2))
print(even_num)


# In[20]:


min(even_num)


# In[21]:


max(even_num)


# In[22]:


sum(even_num)


# In[ ]:




