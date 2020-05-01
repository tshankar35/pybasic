#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Basic Curve of cases due to Covid-19, made during learning about pandas and plotly

import pandas as pd
import plotly.graph_objects as px

data = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise_daily.csv')
fig=px.Figure()
fig.add_trace(px.Scatter(x =data.Date, y=data.JH, mode='lines',name='Jharkhand'))
fig.add_trace(px.Scatter(x=data.Date,y=data.MH,mode='lines',name='Maharashtra'))
fig.add_trace(px.Scatter(x=data.Date,y=data.TN, mode='lines', name='Tamil Nadu'))
fig.add_trace(px.Scatter(x=data.Date,y=data.DL, mode='lines', name='Delhi'))
fig.show()


# In[2]:


import plotly.graph_objects as go
import pandas as pd
import requests

url1=('https://api.covid19india.org/csv/latest/case_time_series.csv')
r1=requests.get(url1)
open('India.csv', 'wb').write(r1.content)
url2=('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv')
r2=requests.get(url2)
open('USA.csv','wb').write(r2.content)
df1=pd.read_csv(r"C:\Users\Tanay-PC\India.csv")
df2=pd.read_csv(r"C:\Users\Tanay-PC\USA.csv")
col_df1=list(df1.columns)
col_df2=list(df2.columns)
col_df1[2]='TotalIN'
df1.columns=col_df1
col_df2[1]='TotalUS'
df2.columns=col_df2
fig = go.Figure()
fig.add_trace(go.Scatter(x=df1.Date, y=df1.TotalIN,
                    mode='lines',
                    name='India Cases'))
fig.add_trace(go.Scatter(x=df2.date, y=df2.TotalUS,
                    mode='lines',
                    name='USA Cases'))
fig.show()


# In[ ]:




