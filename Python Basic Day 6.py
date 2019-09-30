#!/usr/bin/env python
# coding: utf-8

# In[1]:


#changing adding values in list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)


# In[2]:


motorcycles[0] = 'londa'


# In[3]:


print(motorcycles)


# In[6]:


#adding element to lsist
motorcycles.append('hero')
print(motorcycles)

motorcycles.remove[1]
print(motorcycles)
# In[9]:


motorcycles.insert(2,'honda')
print(motorcycles)


# In[10]:


fundamental_python = []
fundamental_python.append('pinnu anusha','anil','ayush gupta','nishant dwivedi','bluepen','sri','sira veluru')


# In[24]:


fundamental_python = []
fundamental_python.append('pinnu anusha')
fundamental_python.append('anil')
fundamental_python.append('ayush gupta')
fundamental_python.append('nishant dwivedi')
fundamental_python.append('bluepen')
fundamental_python.append('sri')
fundamental_python.append('sira veluru')
print(fundamental_python)


# In[25]:


#removing element from list
del fundamental_python[4]
print(fundamental_python)


# In[26]:


motorcycles


# In[27]:


#second method for deleting the the operands from list its POP 
# pop does not delete elements permenantly but delete fucntion deletes the elements permanently
#but pop creates a seperate list of deleted items
pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)


# In[ ]:




