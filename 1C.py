#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

fama_french_filepath = 'C:/Users/tangy/Desktop/data/F-F_Research_Data_Factors.CSV'
msci_usa_filepath = 'C:/Users/tangy/Desktop/data/MSCI USA index.CSV'
msci_usa_value_filepath = 'C:/Users/tangy/Desktop/data/MSCI USA value index.CSV'
msci_usa_min_vol_filepath = 'C:/Users/tangy/Desktop/data/MSCI USA minimum volatility index.CSV'
msci_usa_equal_weighted_filepath = 'C:/Users/tangy/Desktop/data/MSCI USA equal-weighted index.CSV'
msci_usa_momentum_filepath = 'C:/Users/tangy/Desktop/data/MSCI USA momentum index.CSV'

fama_french_data = pd.read_csv(fama_french_filepath)
msci_usa_data = pd.read_csv(msci_usa_filepath)
msci_usa_value_data = pd.read_csv(msci_usa_value_filepath)
msci_usa_min_vol_data = pd.read_csv(msci_usa_min_vol_filepath)
msci_usa_equal_weighted_data = pd.read_csv(msci_usa_equal_weighted_filepath)
msci_usa_momentum_data = pd.read_csv(msci_usa_momentum_filepath)

print("Fama-French Data:")
print(fama_french_data.head())
print("\nMSCI USA Data:")
print(msci_usa_data.head())
print("\nMSCI USA Value Data:")
print(msci_usa_value_data.head())
print("\nMSCI USA Minimum Volatility Data:")
print(msci_usa_min_vol_data.head())
print("\nMSCI USA Equal-Weighted Data:")
print(msci_usa_equal_weighted_data.head())
print("\nMSCI USA Momentum Data:")
print(msci_usa_momentum_data.head())


# In[6]:


def convert_msci_date(date_str):
    if isinstance(date_str, str):
        return datetime.strptime(date_str, '%d-%b-%y').strftime('%Y%m')
    else:
        return 'Unknown'

msci_usa_data['Date'] = msci_usa_data['Date'].apply(convert_msci_date)
msci_usa_value_data['Date'] = msci_usa_value_data['Date'].apply(convert_msci_date)


# In[9]:


def calculate_monthly_returns(df, value_column):
    df[value_column] = pd.to_numeric(df[value_column], errors='coerce')
    df['Monthly_Return'] = df[value_column].pct_change() * 100
    return df

msci_usa_data = calculate_monthly_returns(msci_usa_data, 'USA Standard (Large+Mid Cap)')
msci_usa_value_data = calculate_monthly_returns(msci_usa_value_data, 'USA VALUE Standard (Large+Mid Cap)')
msci_usa_min_vol_data = calculate_monthly_returns(msci_usa_min_vol_data, 'USA MINIMUM VOLATILITY (USD) Standard (Large+Mid Cap)')
msci_usa_equal_weighted_data = calculate_monthly_returns(msci_usa_equal_weighted_data, 'USA EQUAL WEIGHTED Standard (Large+Mid Cap)')
msci_usa_momentum_data = calculate_monthly_returns(msci_usa_momentum_data, 'USA MOMENTUM Standard (Large+Mid Cap)')

print(msci_usa_data.head())


# In[14]:


def convert_msci_date(date_str):
    if isinstance(date_str, str):
        try:
            return datetime.strptime(date_str, '%d-%b-%y').strftime('%Y%m')
        except ValueError:
            return date_str 
    else:
        return date_str

msci_usa_data['Date'] = msci_usa_data['Date'].apply(convert_msci_date)
msci_usa_value_data['Date'] = msci_usa_value_data['Date'].apply(convert_msci_date)
msci_usa_min_vol_data['Date'] = msci_usa_min_vol_data['Date'].apply(convert_msci_date)
msci_usa_equal_weighted_data['Date'] = msci_usa_equal_weighted_data['Date'].apply(convert_msci_date)
msci_usa_momentum_data['Date'] = msci_usa_momentum_data['Date'].apply(convert_msci_date)

msci_usa_data['Date'] = msci_usa_data['Date'].astype(int)
msci_usa_value_data['Date'] = msci_usa_value_data['Date'].astype(int)
msci_usa_min_vol_data['Date'] = msci_usa_min_vol_data['Date'].astype(int)
msci_usa_equal_weighted_data['Date'] = msci_usa_equal_weighted_data['Date'].astype(int)
msci_usa_momentum_data['Date'] = msci_usa_momentum_data['Date'].astype(int)


# In[15]:


msci_usa_data['Date'] = msci_usa_data['Date'].astype(int)
msci_usa_value_data['Date'] = msci_usa_value_data['Date'].astype(int)
msci_usa_min_vol_data['Date'] = msci_usa_min_vol_data['Date'].astype(int)
msci_usa_equal_weighted_data['Date'] = msci_usa_equal_weighted_data['Date'].astype(int)
msci_usa_momentum_data['Date'] = msci_usa_momentum_data['Date'].astype(int)

msci_usa_data = msci_usa_data[(msci_usa_data['Date'] >= start_date) & (msci_usa_data['Date'] <= end_date)]
msci_usa_value_data = msci_usa_value_data[(msci_usa_value_data['Date'] >= start_date) & (msci_usa_value_data['Date'] <= end_date)]
msci_usa_min_vol_data = msci_usa_min_vol_data[(msci_usa_min_vol_data['Date'] >= start_date) & (msci_usa_min_vol_data['Date'] <= end_date)]
msci_usa_equal_weighted_data = msci_usa_equal_weighted_data[(msci_usa_equal_weighted_data['Date'] >= start_date) & (msci_usa_equal_weighted_data['Date'] <= end_date)]
msci_usa_momentum_data = msci_usa_momentum_data[(msci_usa_momentum_data['Date'] >= start_date) & (msci_usa_momentum_data['Date'] <= end_date)]


# In[16]:


import pandas as pd


start_date = 199501
end_date = 202307

msci_usa_data = msci_usa_data[(msci_usa_data['Date'] >= start_date) & (msci_usa_data['Date'] <= end_date)]
msci_usa_value_data = msci_usa_value_data[(msci_usa_value_data['Date'] >= start_date) & (msci_usa_value_data['Date'] <= end_date)]
msci_usa_min_vol_data = msci_usa_min_vol_data[(msci_usa_min_vol_data['Date'] >= start_date) & (msci_usa_min_vol_data['Date'] <= end_date)]
msci_usa_equal_weighted_data = msci_usa_equal_weighted_data[(msci_usa_equal_weighted_data['Date'] >= start_date) & (msci_usa_equal_weighted_data['Date'] <= end_date)]
msci_usa_momentum_data = msci_usa_momentum_data[(msci_usa_momentum_data['Date'] >= start_date) & (msci_usa_momentum_data['Date'] <= end_date)]

# Risk-free rate from Fama-French dataset
fama_french_data = fama_french_data[(fama_french_data['Unnamed: 0'] >= start_date) & (fama_french_data['Unnamed: 0'] <= end_date)]
risk_free_rate = fama_french_data['RF'].mean() / 100  # Converting to decimal

# Function to calculate annualized return and Sharpe Ratio
def calculate_metrics(df):
    avg_monthly_return = df['Monthly_Return'].mean()
    annualized_return = (1 + avg_monthly_return / 100)**12 - 1  # Annualized Return
    annualized_volatility = df['Monthly_Return'].std() * (12**0.5)  # Annual Volatility
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility  # Sharpe Ratio

    return annualized_return, sharpe_ratio

metrics = {
    "MSCI USA": calculate_metrics(msci_usa_data),
    "MSCI USA Value": calculate_metrics(msci_usa_value_data),
    "MSCI USA Min Vol": calculate_metrics(msci_usa_min_vol_data),
    "MSCI USA Equal Weighted": calculate_metrics(msci_usa_equal_weighted_data),
    "MSCI USA Momentum": calculate_metrics(msci_usa_momentum_data)
}

metrics_df = pd.DataFrame(metrics, index=["Annualized Return", "Sharpe Ratio"]).T
print(metrics_df)


# In[17]:


import matplotlib.pyplot as plt

metrics_df.plot(kind='bar', subplots=True, layout=(2, 1), figsize=(10, 8), legend=False)

plt.subplots_adjust(hspace=0.5)
plt.suptitle('MSCI Index Performance Analysis (1995 - 2023)')

plt.subplot(2, 1, 1)
plt.ylabel('Annualized Return')
plt.xticks(rotation=45)

plt.subplot(2, 1, 2)
plt.ylabel('Sharpe Ratio')
plt.xticks(rotation=45)

plt.show()


# In[18]:


msci_multi_factor = (msci_usa_value_data['Monthly_Return'] + 
                     msci_usa_min_vol_data['Monthly_Return'] + 
                     msci_usa_equal_weighted_data['Monthly_Return'] + 
                     msci_usa_momentum_data['Monthly_Return']) / 4

msci_multi_factor_data = pd.DataFrame({'Date': msci_usa_value_data['Date'], 'Monthly_Return': msci_multi_factor})

multi_factor_metrics = calculate_metrics(msci_multi_factor_data)

metrics_df.loc['MSCI Multi-Factor'] = multi_factor_metrics

print(metrics_df)


# In[ ]:




