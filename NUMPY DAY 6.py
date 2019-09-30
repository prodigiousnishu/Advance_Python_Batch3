#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[ ]:


#rows col operation
#in a given 2 day array  ----> axs = 0 ----> cols
#                       ----->axis = 1 -----> rows


# In[4]:


import numpy as np
numbers = np.arange(12).reshape(3,4)


# In[5]:


import numpy as np
numbers = np.arange(12).reshape(3,4)
finding sum of thnumbers


# In[6]:


#finding sum of the column we do axis = 0
numbers.sum(axis = 0)


# In[7]:


#finding sum of the rows we do axis = 
numbers.sum(axis = 1)


# In[12]:


numbers.min(axis = 0)


# In[9]:


numbers.max(axis = 1)


# In[11]:


#gives the indes of the array first it gives us the min of column by axis = 0 and then the first potition of the min column values
numbers.min(axis = 0)[1]


# In[15]:



import numpy as np
numbers = np.arange(12).reshape(3,4)[0]
numbers



# In[16]:


import numpy as np
numbers = np.arange(12).reshape(3,4)[1]
numbers


# In[19]:


#statistical function
tset_scores = np.array([32.32,56.98,21.52,44.32,55.63,13.25,43.47,43.34])


# In[22]:


#statistical function
test_scores = np.array([32.32,56.98,21.52,44.32,55.63,13.25,43.47,43.34])

print('mean information scores of the student')
print(np.mean(test_scores))


# In[23]:


print(np.median(test_scores))


# In[ ]:





# In[ ]:




