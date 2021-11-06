#!/usr/bin/env python
# coding: utf-8

# In[19]:


# modules: -------------------------------------------------------------------
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind_from_stats
from scipy.stats import norm
from Stats507_hw4_helper import ci_prop
from Stats507_hw4_helper import ci_mean
from numpy import arange
import itertools
from scipy.stats import binom
from collections import defaultdict
import math
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import datetime


# Ran Yan ranyan@umich.edu

# # Question 0
# 
# reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html

# ## Time Series
# 
# - pandas contains extensive capabilities and features for working with time series data for all domains. 
# - can parse time series information in different formats and sources
#     - see example 1 below
# - can generate sequences of fixed-frequency dates and time spans
#     - see example 2 below
# - ca manipulating and converting date times with timezone information
#     - see example 3 below

# In[25]:


# example 1
dti = pd.to_datetime(
    ["5/20/2000", np.datetime64("2000-05-20"), datetime.datetime(2000, 5, 20)]
)
dti


# In[29]:


# example 2
dti = pd.date_range("2000-01", periods=5, freq="D")
dti


# In[30]:


# example 3
dti = dti.tz_localize("UTC")
dti


# ## Convert to Timestamps
# 
# - when convert to timestamps, convert series to series and convert list-like data to DatetimeIndex
# - return a single timestamp if pass a string
# - can use format argument to ensure specific parsing, here is an example below

# In[31]:


pd.to_datetime("2021/10/23", format="%Y/%m/%d")


# ## Some useful Time Series Functions
# 
# - `between_time` 
#     - to select rows in data frame that are only between certain time range
#     - here is an example below to select time from 9:00 to 10:00
# - `date_range`
#     - convert timestamp to a 'unix' epoch
# - `bdate_range`
#     - create DatetimeIndex for in a range of business days

# In[23]:


rng = pd.date_range('2/3/2000', periods=24, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts.iloc[ts.index.indexer_between_time(datetime.time(9), datetime.time(10))]


# In[33]:


stamps = pd.date_range("2021-10-23 20:15:05", periods=2, freq="H")
stamps


# In[34]:


start = datetime.datetime(2021, 10, 20)
end = datetime.datetime(2021, 10, 23)
index = pd.bdate_range(start, end)
index

