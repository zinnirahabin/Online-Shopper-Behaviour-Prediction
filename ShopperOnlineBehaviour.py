#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("C:/Users/Zimirah/Documents/UNITEN/SEM 5/Machine Learning/Online Shopper Behaviour.csv")

df


# In[2]:


df.info()
df.isnull().sum()


# In[3]:


df = df.drop(columns=["What's the last item you purchased?"])


# In[4]:


df = df.dropna()


# In[5]:


df.info()


# In[6]:


df.columns = df.columns.str.strip()


# In[7]:


df.info()


# In[8]:


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = le.fit_transform(df[column])


# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


import pandas as pd

df = pd.read_csv("C:/Users/Zimirah/Documents/UNITEN/SEM 5/Machine Learning/Online Shopper Behaviour.csv")


# In[6]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x="Did you complete your purchase ?", data=df)
plt.title("Purchase Completion Distribution")
plt.show()


# In[ ]:




