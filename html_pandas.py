#!/usr/bin/env python
# coding: utf-8

# In[24]:


def configure_plotly_browser_state():
  import IPython
  display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths: {
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-1.5.1.min.js?noext',
            },
          });
        </script>
        '''))
  
configure_plotly_browser_state()
init_notebook_mode(connected=False)


# In[39]:


import numpy as np
import pandas as pd
import csv
# 匯入plotly套件，以便繪製視覺化圖形
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go


data1 = pd.read_csv('gdp_taiwan.csv')
data2 = pd.read_csv('gdp_world.csv')

Taiwan = data1.loc[0]
country = data2.loc[117]

print(country)

years = np.linspace(1960, 2020, 58) # 製造從 1960 至 2020 的年

trace1 = go.Scatter(
    x = years,
    y = Taiwan*1000000,
    mode = 'lines+markers',
    name = '臺灣'
)

trace2 = go.Scatter(
    x = years,
    y = country,
    mode = 'lines+markers',
    name = '日本'
)

data = [trace1, trace2]

iplot(data, filename='scatter-mode')


# In[36]:


country


# In[34]:


data2


# In[ ]:


np.arrany(:)

