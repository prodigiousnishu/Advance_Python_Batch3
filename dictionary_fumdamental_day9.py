#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Introduction to Dictionary

#Key and value pair

#need to created FB account

#username & password

#username=Nishant15
#password = XXXXXX --- then only account unlocks 

#otherwise password is not correct

#It is security based data type all the passwords are stored in dictionary datatype in backend

#for representin dict = {}
#for list = []
#for tuple = ()
#str = '',""

new ={'name':'sana','age':7,'standard':6}
print(new)


# In[8]:


print(new['name'])


# In[9]:


#if want to print the value which are not present in dictionary

print(new['surname'])

#you will get error:if want to print the value which are not present in dictionary


# In[ ]:


#Dictionary is a mutable datatype:we can able to modify it when its get assigned

#every time when are password expired we reset it and it is in backend stores in dictionary thus it is immutable


# In[11]:


new ={'name':'sana','age':7,'standard':6}

new['age']=8 #upadted value
new['School'] = 'DPS'#added the column in dictionary

print(new)


# In[12]:


#How to remove the values in dictionary

del new['standard']
print(new)


# In[14]:


#to clear all the entries of dict

new.clear()
print(new)

#to delte full dictionary

del new
print(new)


# In[ ]:




