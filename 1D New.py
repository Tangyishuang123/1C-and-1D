#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

file_ff_factors = 'C:/Users/tangy/Desktop/data/F-F_Research_Data_Factors.CSV'

df_ff_factors = pd.read_csv(file_ff_factors, skiprows=3)

print(df_ff_factors.head())


# In[8]:


import pandas as pd

base_path = 'C:/Users/tangy/Desktop/data/'

file_ff_factors = base_path + 'F-F_Research_Data_Factors.CSV'
file_msci_usa_index = base_path + 'MSCI USA index.CSV'
file_msci_value_index = base_path + 'MSCI USA value index.CSV'
file_msci_min_vol_index = base_path + 'MSCI USA minimum volatility index.CSV'
file_msci_equal_weighted_index = base_path + 'MSCI USA equal-weighted index.CSV'
file_msci_momentum_index = base_path + 'MSCI USA momentum index.CSV'
file_ff_portfolios_beta = base_path + 'FF - portfolios sorted on beta.CSV'
file_msci_factor_totret_index = base_path + 'MSCI - factor totret index.CSV'

df_ff_factors = pd.read_csv(file_ff_factors, skiprows=3)
df_msci_usa_index = pd.read_csv(file_msci_usa_index)
df_msci_value_index = pd.read_csv(file_msci_value_index)
df_msci_min_vol_index = pd.read_csv(file_msci_min_vol_index)
df_msci_equal_weighted_index = pd.read_csv(file_msci_equal_weighted_index)
df_msci_momentum_index = pd.read_csv(file_msci_momentum_index)
df_ff_portfolios_beta = pd.read_csv(file_ff_portfolios_beta, encoding='ISO-8859-1')
df_msci_factor_totret_index = pd.read_csv(file_msci_factor_totret_index, encoding='ISO-8859-1')

print("Fama-French Factors Data:\n", df_ff_factors.head())
print("\nMSCI USA Index Data:\n", df_msci_usa_index.head())
print("\nMSCI USA Value Index Data:\n", df_msci_value_index.head())
print("\nMSCI USA Minimum Volatility Index Data:\n", df_msci_min_vol_index.head())
print("\nMSCI USA Equal-Weighted Index Data:\n", df_msci_equal_weighted_index.head())
print("\nMSCI USA Momentum Index Data:\n", df_msci_momentum_index.head())
print("\nFama-French Portfolios Sorted on Beta:\n", df_ff_portfolios_beta.head())
print("\nMSCI Factor Total Return Index:\n", df_msci_factor_totret_index.head())


# In[9]:


df_ff_factors['Date'] = pd.to_datetime(df_ff_factors.iloc[:, 0], format='%Y%m').dt.to_period('M')
df_msci_usa_index['Date'] = pd.to_datetime(df_msci_usa_index['Date'], dayfirst=True).dt.to_period('M')
df_msci_value_index['Date'] = pd.to_datetime(df_msci_value_index['Date'], dayfirst=True).dt.to_period('M')
df_msci_min_vol_index['Date'] = pd.to_datetime(df_msci_min_vol_index['Date'], dayfirst=True).dt.to_period('M')
df_msci_equal_weighted_index['Date'] = pd.to_datetime(df_msci_equal_weighted_index['Date'], dayfirst=True).dt.to_period('M')
df_msci_momentum_index['Date'] = pd.to_datetime(df_msci_momentum_index['Date'], dayfirst=True).dt.to_period('M')
df_msci_factor_totret_index['Date'] = pd.to_datetime(df_msci_factor_totret_index['Date'], dayfirst=True).dt.to_period('M')


print(df_msci_factor_totret_index.dtypes)


# In[10]:


def convert_to_float(s):
    try:
        return float(s.replace(',', ''))
    except ValueError:
        return None

for col in df_msci_factor_totret_index.columns[1:]:
    df_msci_factor_totret_index[col] = df_msci_factor_totret_index[col].apply(convert_to_float)

df_msci_factor_totret_index = df_msci_factor_totret_index.set_index('Date')
df_msci_returns = df_msci_factor_totret_index.pct_change().dropna()

print(df_msci_returns.head())


# In[11]:


df_msci_spreads = pd.DataFrame()
df_msci_spreads['Value Spread'] = df_msci_returns['USA VALUE Standard (Large+Mid Cap)'] - df_msci_returns['USA Standard (Large+Mid Cap)']
df_msci_spreads['Min Vol Spread'] = df_msci_returns['USA MINIMUM VOLATILITY (USD) Standard (Large+Mid Cap)'] - df_msci_returns['USA Standard (Large+Mid Cap)']
df_msci_spreads['Equal Weighted Spread'] = df_msci_returns['USA EQUAL WEIGHTED Standard (Large+Mid Cap)'] - df_msci_returns['USA Standard (Large+Mid Cap)']
df_msci_spreads['Momentum Spread'] = df_msci_returns['USA MOMENTUM Standard (Large+Mid Cap)'] - df_msci_returns['USA Standard (Large+Mid Cap)']

print(df_msci_spreads.head())


# In[20]:


print(df_ff_factors.head())


# In[22]:


print("Fama-French Factors Date Range:\n", df_ff_factors.index.min(), "to", df_ff_factors.index.max())

print("MSCI Factor Spreads Date Range:\n", df_msci_spreads.index.min(), "to", df_msci_spreads.index.max())


# In[25]:


print("Fama-French Factors Descriptive Statistics:\n", df_aligned_ff.describe())

print("MSCI Factor Spreads Descriptive Statistics:\n", df_aligned_msci.describe())


# In[30]:


import numpy as np

manual_correlation_results = {}

for msci_col in df_aligned_msci.columns:
    for ff_col in ['SMB', 'HML']:
        correlation = np.corrcoef(df_aligned_msci[msci_col], df_aligned_ff[ff_col])[0, 1]
        key = f'{msci_col} vs {ff_col}'
        manual_correlation_results[key] = correlation

for key, value in manual_correlation_results.items():
    print(f"{key}: {value}")


# In[48]:


def correlation(series1, series2):
    valid_index = series1.notna() & series2.notna()
    if valid_index.any():
        return np.corrcoef(series1[valid_index], series2[valid_index])[0, 1]
    else:
        return np.nan

correlation_results = {}

for msci_col in df_msci_spreads.columns:
    correlation = correlation(df_aligned_mom['MOM'], df_msci_spreads[msci_col])
    key = f'MOM vs {msci_col}'
    correlation_results[key] = correlation

print("Calculated Correlations:")
for key, value in manual_correlation_results.items():
    print(f"{key}: {value}")


# In[52]:


def correlation(series1, series2):
    valid_index = series1.notna() & series2.notna()
    if valid_index.any():
        return np.corrcoef(series1[valid_index], series2[valid_index])[0, 1]
    else:
        return np.nan

correlation_results = {}

for msci_col in df_msci_spreads.columns:
    correlation = correlation(df_low_vs_high_beta['Low_vs_High_Beta'], df_msci_spreads_aligned[msci_col])
    key = f'Low_vs_High_Beta vs {msci_col}'
    correlation_results[key] = correlation

print("Calculated Correlations with Low vs. High Beta Factor:")
for key, value in correlation_results.items():
    print(f"{key}: {value}")


# In[ ]:




