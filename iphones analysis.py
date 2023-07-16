#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


# In[2]:


df=pd.read_csv("apple_products.csv")
df


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df.describe()


# In[7]:


df.head(30)


# In[15]:


highest_rated=df.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
highest_rated["Product Name"]


# In[18]:


iphones=highest_rated["Product Name"].value_counts()
label=iphones.index
counts=highest_rated["Number Of Ratings"]
figure=px.bar(highest_rated,x=label,y=counts,title="Number of rating on highest rated of i phones")
figure.show()


# In[19]:


iphones=highest_rated["Product Name"].value_counts()
label=iphones.index
counts=highest_rated["Number Of Reviews"]
figure=px.bar(highest_rated,x=label,y=counts,title="Number Of Reviews of highest rated of i phones")
figure.show()


# In[22]:


figure=px.scatter(df,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",trendline="ols",
                  title="Relation between Number of Rating and Sale Price")
figure.show()


# In[24]:


figure=px.scatter(df,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",trendline="ols",
                  title="Relation between Number of Rating and Discount Percentage")
figure.show()


# In[32]:


figure=px.scatter(df,x="Mrp",y="Sale Price",size="Discount Percentage",trendline="ols",
                  title="Relation between Mrp and Sale Price")
figure.show()


# In[ ]:




