#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import pandas as pd
import nltk
import numpy as np
from nltk.corpus import stopwords
import string
string.punctuation


# In[2]:


import pandas as pd
df=pd.read_csv("/Users/divyaj_podar/Final_set.csv")
#df.head()
#df[df['Brand']=='samsung']
#df.info()


# In[3]:


df_6t=df[df['Model']=='6t']
df_s10=df[df['Model']=='s10']
df_pixel3=df[df['Model']=='pixel3']
df_xs=df[df['Model']=='xs']

df=df.drop_duplicates(keep="first")
df_s10 = df_s10.drop_duplicates (keep = "first")


# In[4]:


def tokenize(text2):
    # takes a list of comment strings and tokenizes
    new=[]
    tokens=[]
    count=0
    for text in text2:
        pattern=r'\w[\w\'-]*\w'      
        tokens=nltk.regexp_tokenize(text, pattern)
        tokens=[tokens.lower() for tokens in tokens]
        new+=tokens 
        count+=1
    return nltk.pos_tag(new)


# In[5]:


tagged_tokens = tokenize (df_s10["commentText"])


# In[6]:


bigrams=list(nltk.bigrams(tagged_tokens))

# gives bigrams where nouns are followed by adj

phrases=[ (x[0] + ' ' + y[0]) for (x,y) in bigrams          if x[1].startswith('JJ' or 'JJS' or 'JJR')          and y[1].startswith('NN' or 'NNP' or 'NNS' or 'NNPS')]

phrases


# In[7]:


word_dist=nltk.FreqDist(phrases)
#word_dist

# get the most frequent items
print("top 30 bigrams:", word_dist.most_common(30))


# In[ ]:




