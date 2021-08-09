import sys
sys.path.append('../')
from preprocess import transform 
from feature import extract  
import glob
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import re 
import pandas as pd
import os 

for ctu_file in glob.glob("../CTU-13-Dataset/*.binetflow"):

  pd.set_option('display.max_columns', 200)
  pd.set_option('display.max_rows', 100)
  pd.set_option('display.min_rows', 100)
  pd.set_option('display.expand_frame_repr', True)

  print("processing {}".format(ctu_file)) 

  df = transform.insertBooleanMaliciousColumn(ctu_file, 'Label', writeoutputfile=False)      
  
  df = extract.mapProtocol(df)

  df['DstAddr'] = extract.IPv4toCount(df['DstAddr']) 

  df = extract.mapDestPort(df)

  # Grab features of intrest to use in ML 
  features = df[["Dur", "Proto",  "Dport", "TotPkts", "DstAddr", "botnet"]]

  print(features.head())
  columns = list(features)
  
  for i in columns:
    # replace any non-numeric with Nan
    if(features[i].dtype == object): 
 
      try:
        print("Replacing non-numeric values in column" + i )  
        features[i] =  np.where( features[i].str.isnumeric(), features[i], np.nan)
      except:
        print(i) 
        print("Unexpected error:", sys.exc_info()[0])

  #print(features.head())
  #print(features.shape)
  #print (df.dtypes)

  print(features.head()) 
  features = features.fillna(np.nan)

  features = features.dropna()
  print(features.shape)


  writeoutputfile = True
  if writeoutputfile:
    path, filename = os.path.split(os.path.abspath(ctu_file))

    outputfile = "./run/out/{}/{}_features.csv".format("features", os.path.splitext(filename)[0])
 
    print("writing out {} ".format(outputfile))

    features.to_csv(outputfile, index=False) 
  


  




