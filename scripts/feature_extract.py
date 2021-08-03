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

  print("processing {}".format(ctu_file)) 

  df = transform.insertBooleanMaliciousColumn(ctu_file, 'Label', writeoutputfile=False)      

  # Do something with new data frame such as scatter plot via pandas and matlab
  print(df.head())

  print("splitting IPv4 into 4 octet fields") 
  df_ipv4_split = extract.splitIPv4Add(df["DstAddr"])

  df = df.join(df_ipv4_split)
  
  print("mapping protocol to integers") 
  df = extract.mapProtocol(df)

  # Grab features of intrest to use in ML 
  features = df[["Dur", "Proto",  "Dport", "TotPkts", "DstAddr_octet1", "DstAddr_octet2", "DstAddr_octet3", "DstAddr_octet4", "botnet"]]

  print(features.head())
  #print (df.dtypes)

  writeoutputfile = True
  if writeoutputfile:
   path, filename = os.path.split(os.path.abspath(ctu_file))

   outputfile = "./run/out/{}/{}_features.csv".format("features", os.path.splitext(filename)[0])
 
   print("writing out {} ".format(outputfile))

   features.to_csv(outputfile, index=False) 
  


  




