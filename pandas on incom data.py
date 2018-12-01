#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


income=pd.read_csv(r"C:\Users\ss\Downloads\income.csv")


# In[3]:


income


# In[4]:


income.columns


# In[5]:


income.columns[0:2]


# In[6]:


income['State']


# In[7]:


income['State'].dtypes


# In[8]:


income.Y2008=income.Y2008.astype(float)


# In[9]:


income.dtypes


# In[11]:


income.shape


# In[13]:


income.shape[0]


# In[14]:


income.shape[1]


# In[15]:


income.head()


# In[16]:


income.head(10)


# In[17]:


income.tail()


# In[18]:


income.tail(15)


# In[19]:


income.iloc[0:5]


# In[20]:


income.Index.unique()


# In[22]:


pd.crosstab(income.Index,income.State)


# In[26]:


income.Index.value_counts(ascending=True)


# In[27]:


income.Index.value_counts()


# In[33]:


income.sample(n=5)
income.sample(frac=0.1)


# In[48]:


income.iloc[:,["Index","State","Y2008"]]


# In[50]:


income.iloc[:,0:5]


# In[52]:



income[["Index","State","Y2008"]]


# In[53]:


data = pd.DataFrame({"A" : ["John","Mary","Julia","Kenny","Henry"], "B" : ["Libra","Capricorn","Aries","Scorpio","Aquarius"]})
data 


# In[54]:


data=pd.DataFrame({"A":["harry","charan","ankit","masthan"]})


# In[55]:


data


# In[56]:


data.columns=["Names"]


# In[57]:


data


# In[58]:


data.rename(columns={"Names":"Name"})


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




