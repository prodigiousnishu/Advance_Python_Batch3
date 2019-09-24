#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[ ]:


#NEED TO PRINT EVEN NUMBERS TILL 20 BY USING NUMPY


# In[4]:


X = NP.arange(2,21,2)


# In[5]:


X = np.arrange(2,21,2)


# In[7]:


import numpy as np

X = np.arange(2,21,2)
X
#normal python this was done using RANGE(x,y,stepcount) function-----> arange(x,y,stepcount)
# in arange function--> last value is exclusive


# In[9]:


# by using float values
array_of_floats = np.arange(0,2,0.3)
array_of_floats


# In[13]:


#2dimensional array
import numpy as np
array_2d = ([(2,4,6),(3,5,7)])
array_2d
array_2d.shape


# In[22]:


import numpy as np
array_2d = ([2,4,6],[3,5,7])
array_2d
array_2d.shape


# In[15]:


a =np.arange(6)
print(a)


# In[16]:


array_nd = np.arange(6).reshape(2,3)
array_nd


# In[18]:


a =np.arange(6)
print(a)
a.shape


# In[19]:


array_nd = np.arange(100).reshape(10)
array_nd


# In[20]:


array_nd = np.arange(100).reshape(10,10)
array_nd
#multiple we need to mailtain  10*10 = 100 or 2 * 50
#6 = 2*3 reshaping should end into 6 or 10 or multiple


# In[23]:


import numpy as np
array_2d = np.([(2,4,6),(3,5,7)])
array_2d
array_2d.shape


# In[24]:


import numpy as np
array_2d = np.array([(2,4,6),(3,5,7)])
array_2d
array_2d.shape


# In[25]:


array_2d = np.array([(2,4,6),(3,5,7)])
array_2d


# In[26]:


my__1D_array = numpy.array([1, 2, 3, 4, 5])
my_1D_array
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns


# In[27]:


import numpy as numpy
my__1D_array = numpy.array([1, 2, 3, 4, 5])
my__1D_array


# In[28]:


import numpy as np

X = np.arange(2,21,2)
X
#normal python this was done using RANGE(x,y,stepcount) function-----> arange(x,y,stepcount)
# in arange function--> last value is exclusive


# In[29]:


import numpy as np

X = np.linspace(2,20,10)
X
#normal python this was done using RANGE(x,y,stepcount) function-----> arange(x,y,stepcount)
# in arange function--> last value is exclusive


# In[30]:


type([0])


# In[31]:


type(X[0])


# In[ ]:


# for options on functions type --X.presstab


# In[ ]:


from skimage import io
photo = io.imread('PY.jpg')
type(photo)


# In[ ]:


photo.shape


# In[36]:


from skimage import io
photo = io.imread('PY.jpg')
import matplotlib.pyplot as plt
plt.imshow(photo)


# In[ ]:




