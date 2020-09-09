#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[3]:


sns.get_dataset_names()


# In[18]:


data = sns.load_dataset('diamonds')


# In[19]:


import pandas as pd

df = pd.DataFrame(data)


# In[20]:


df.columns


# In[21]:


df.head()


# In[43]:


number = df.cut.value_counts().rename_axis('Diamond Cut').reset_index(name='Number of Values')


# In[24]:


diamonds = sns.load_dataset('diamonds')


# In[44]:


number


# In[48]:


plot = sns.barplot("Diamond Cut","Number of Values",data=number)


# In[50]:


tips = sns.load_dataset('tips')


# In[51]:


tips = pd.DataFrame(tips)


# In[52]:


tips.info()


# In[56]:


tips.total_bill.sum(),tips.day.count()


# In[59]:


tips.total_bill.max(),tips.total_bill.min(),tips.total_bill.mean()


# In[74]:


#tips.plot.hist(bins=10)


# In[85]:


#tips.hist(by=tips['total_bill'],bins = 10)
tips.day.value_counts().plot(kind = 'bar',color='red')


# In[75]:


import matplotlib.pyplot as plt


# In[88]:


x = tips.total_bill + tips.tip
num_bins = 10
n, bins, patches = plt.hist(x, num_bins, facecolor='black', alpha=0.5)
plt.show()


# In[90]:


tips['totalbill'] = tips.total_bill + tips.tip


# In[91]:


tips


# In[106]:


tips.sex.value_counts().plot(kind='pie',figsize=(5, 8),autopct='%1.1f%%', startangle=90)


# In[100]:


tips.day.value_counts().plot(kind='pie',figsize=(5, 5),autopct='%1.1f%%', startangle=90)


# In[110]:


tips.time.value_counts().plot(kind='pie',figsize=(5, 5),autopct='%1.1f%%', startangle=90,colors=['green','yellow'])


# In[112]:


tips['size'].value_counts().plot(kind='pie',figsize=(5, 5),autopct='%1.1f%%', startangle=90)


# In[113]:


sns.get_dataset_names()


# In[116]:


mpg = pd.DataFrame(sns.load_dataset('mpg'))


# In[117]:


mpg.info()


# In[121]:


mpg.cylinders.unique()

