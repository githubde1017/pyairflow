#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a)
print(np.where(a<3))


# In[5]:


x = np.arange(9.).reshape(3, 3)
print(x)
np.where( x > 5 )


# In[8]:


x[np.where( x > 3.0 )]               # Note: result is 1D.
np.where(x < 5, x, -1)               # Note: broadcasting.

