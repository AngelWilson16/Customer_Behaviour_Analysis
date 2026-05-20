#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

df = pd.read_csv('customer_shopping_behavior.csv')


# In[5]:


df.head()


# In[6]:


df.describe(include= 'all')


# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# In[9]:


df['Review Rating'].hist()


# In[10]:


df['Review Rating'].skew()


# In[11]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[12]:


df.isnull().sum()


# In[13]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[14]:


df.columns


# In[16]:


#Feature Engineering
labels = ['Young Adult','Adult','Middle_aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels = labels)


# In[17]:


df[['age','age_group']].head(10)


# In[18]:


# Create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly': 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months': 90
}

df['Purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[19]:


df[['Purchase_frequency_days', 'frequency_of_purchases']].head(10)


# In[20]:


df[['discount_applied','promo_code_used']].head(10)


# In[21]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[22]:


df = df.drop('promo_code_used', axis=1)


# In[23]:


df.columns


# In[3]:


pip install psycopg2-binary sqlalchemy


# In[27]:


from sqlalchemy import create_engine
username = "postgres"
password = "angel%40123%23"
host = "localhost"
port = "5432"
database = "customer_behavior"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# load dataframe into Postgresql
table_name = "customer"

df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[23]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




