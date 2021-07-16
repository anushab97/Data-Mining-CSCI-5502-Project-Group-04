import sys
sys.path.append('../')
from preprocess import transform 
import glob


for ctu_file in glob.glob("../CTU-13-Dataset/*.binetflow"):

  print("processing {}".format(ctu_file)) 

  ctu_dataframe = transform.insertBooleanMaliciousColumn(ctu_file, 'Label', writeoutputfile=False)      

  # Do something with new data frame such as scatter plot via pandas and matlab

