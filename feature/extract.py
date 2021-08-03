import pandas as pd
import numpy as np
import re
import os

# Various functions to extract features

def splitIPv4Add(df_series):

  ''' Function to split a IPv4 Pandas Series into 4 binary numbers for ML processing 
      Returns Data Frame with split IPv4

      Arguments 
      ----------

     df:  Data Frame iSeries containing the IPv4 (e.g. dest address)

  '''

  df_series = df_series.str.split('.', expand=True).rename(
         columns={0:'DstAddr_octet1', 1:'DstAddr_octet2', 2:'DstAddr_octet3', 3:'DstAddr_octet4'})

  return df_series 


# Map protocol to a specific list 
def mapProtocol(df):

  ''' Function to map Protocol into integer values binary numbers for ML processing 
      Returns Data frame

      Arguments 
      ----------

      df:  Data Frame

      '''

  # Define map of values that of a intrest. All other values will be 0
  replace_map = {'Proto': {'tcp': 1, 'udp': 2, 'icmp': 3}}

  df.replace(replace_map, inplace=True)
 
  # replace other not in map with 0  
  df['Proto'] = np.where( df['Proto'].str.isnumeric(), df['Proto'], 0 )

  return df
