import pandas as pd
import numpy as np
import re
import os 

def insertBooleanMaliciousColumn(binetflow, colindex, writeoutputfile=False):

  ''' Function to add another column as bolean value whether Label contains botnet 
      returns a pandas DataFrame object

  Arguments 
  ----------

  binetflow:  Fully Qualified File Name of .binetflow data
  colindex:   Column index to search for botnet string. 
  outputfile: set to True to write out file to same dir as input directoru 


  CTU-13 base format (*.binetflow type files)

  StartTime
  Dur
  Proto
  SrcAddr
  Sport
  Dir
  DstAddr
  Dport
  State
  sTos
  dTos
  TotPkts
  TotBytes
  SrcBytes
  Label

  '''

  p = re.compile('.+botnet.+', re.IGNORECASE)

  ctu = pd.read_csv(binetflow)

  ctu['botnet'] = np.where( ctu['Label'].str.match((p)), 1, 0)

  bot_flow_percentage =  (len(np.where(ctu['botnet']==1)[0])/np.shape(ctu)[0]) * 100

  # Print some useful processing stats 
  print("{} botnet flows found in {} total flows which is {} percent ".format( len(np.where(ctu['botnet']==1)[0]), np.shape(ctu)[0], bot_flow_percentage )) 

  # If true write out files
  if writeoutputfile:
   path, filename = os.path.split(os.path.abspath(binetflow))
  
   outputfile = "./run/out/{}/{}_botcode.binetflow".format("CTU-13", os.path.splitext(filename)[0])
  
   print("writing out {} ".format(outputfile))

   ctu.to_csv(outputfile)

  return ctu 
