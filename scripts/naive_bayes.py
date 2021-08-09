import sys
sys.path.append('../')
from preprocess import transform 
from feature import extract  
from ml import naive_bayes  
import glob
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import re 
import pandas as pd
import os 


run_all_scenarios      = True
run_single_scenario    = False
run_combined_scenarios = False


if run_all_scenarios:

  for i in range(1, 14):

    df = None
    scenario = i
    print("processing scenario {} ".format(scenario))
    path = "./run/out/features/{}*.csv".format(scenario)
    df = pd.concat(map(pd.read_csv, glob.glob(path)), ignore_index= True)
    naive_bayes.evenOdd(df, scenario)

 
if run_single_scenario:

  scenario = "11"
  df = None
  print("processing scenario {} ".format(scenario))
  path = "./run/out/features/{}*.csv".format(scenario)
  df = pd.concat(map(pd.read_csv, glob.glob(path)), ignore_index= True)
  naive_bayes.evenOdd(df, scenario)

if run_combined_scenarios:

  scenario = "1-13"
  df = None
  print("processing scenario {} ".format(scenario))
  path = "./run/out/features/*.csv"
  df = pd.concat(map(pd.read_csv, glob.glob(path)), ignore_index= True)
  naive_bayes.evenOdd(df, scenario)
