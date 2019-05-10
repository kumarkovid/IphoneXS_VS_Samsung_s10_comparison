#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df1 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/7YKjLzlc-hY.csv', header=0)


# In[5]:


df2 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/BJrsmM6aEYE.csv', header=0)


# In[23]:


df3 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/KI6ZJTSja4s.csv', header=0, engine = 'python')


# In[8]:


df4 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/XFckmtISfJk.csv', header=0)


# In[9]:


df5 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/_6-XjSvbJsE.csv', header=0)


# In[10]:


df6 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/LRh_iVXulXk.csv', header=0)


# In[11]:


df7 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/t9R7xx0joOU.csv', header=0)


# In[12]:


df8 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/YAF9BWpzwvI.csv', header=0)


# In[13]:


df9 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/9oEmm2h_9dc.csv', header=0)


# In[14]:


df10 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/nqNKbkdoR6I.csv', header=0)


# In[15]:


df11 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/7_P44IER6KI.csv', header=0)


# In[16]:


df12 = pd.read_csv('/Users/divyaj_podar/Desktop/URL_all_data/Gsa6JotlOTA.csv', header=0)


# In[25]:


final_set = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12])


# In[28]:


final_set.to_csv('final_set.csv', header=True, index=False)


# In[ ]:




