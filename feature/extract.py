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


def IPv4toCount(df_series):


  ip_counts = df_series.value_counts()
  df_series = df_series.apply(lambda x: ip_counts[x])

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

def mapDestPort(df): 


  ''' Function to replace common ports.  This first re-assigns the common ports to the character name. 
     Then changes all numeric to 0 and then maps new in new port assignments 
  ''' 

  replace_map = {'Dport': {'53': 'dns', '13363': 'nonres1', '80': 'http', '443': 'https', '22': 'ssh', '6881': 'bittorrent1', '3389': 'rdp', '1712': 'dnap', '123': 'ntp',  '161': 'snmp' }}

  df.replace(replace_map, inplace=True)

  df['Dport'] = np.where( df['Dport'].str.isnumeric(), 0, df['Dport'])

  replace_map_to_int = {'Dport': {'dns': 1, 'nonres1': 2,  'http': 3, 'https': 4, 'ssh': 5, 'bittorrent1': 6,  'rdp': 7,  'dnap': 8, 'ntp': 9,  
                         'snmp': 10 }}
  
  df.replace(replace_map_to_int, inplace=True)
 
  return df

  


