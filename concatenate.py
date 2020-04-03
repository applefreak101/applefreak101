#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


APRIL = pd.read_csv("Sales_April_2019.csv")


# In[6]:


APRIL.head()


# In[7]:


JANUARY = pd.read_csv("Sales_January_2019.csv")


# In[8]:


FEBRUARY = pd.read_csv("Sales_February_2019.csv")


# In[9]:


MARCH = pd.read_csv("Sales_March_2019.csv")


# In[10]:


MAY = pd.read_csv("Sales_May_2019.csv")


# In[11]:


JUNE = pd.read_csv("Sales_June_2019.csv")


# In[12]:


JULY = pd.read_csv("Sales_July_2019.csv")


# In[13]:


AUGUST = pd.read_csv("Sales_August_2019.csv")


# In[14]:


SEPTEMBER = pd.read_csv("Sales_September_2019.csv")


# In[15]:


OCTOBER = pd.read_csv("Sales_October_2019.csv")


# In[16]:


NOVEMBER = pd.read_csv("Sales_November_2019.csv")


# In[17]:


DECEMBER = pd.read_csv("Sales_December_2019.csv")


# In[18]:


values1=JANUARY[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[19]:


values2=FEBRUARY[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[20]:


values3=MARCH[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[21]:


values4=APRIL[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[22]:


values5=MAY[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[23]:


values6=JUNE[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[24]:


values7=JULY[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[25]:


values8=AUGUST[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[26]:


values9=SEPTEMBER[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[28]:


values10=OCTOBER[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[27]:


values11=NOVEMBER[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[30]:


values12=DECEMBER[['Order ID','Product','Quantity Ordered','Price Each','Order Date','Purchase Address']]


# In[31]:


dataframes =[values1,values2,values3,values4,values5,values6,values7,values8,values9,values10,values11,values12]


# In[32]:


join =pd.concat(dataframes)


# In[36]:


join.to_excel("combined.xlsx")


# In[ ]:




