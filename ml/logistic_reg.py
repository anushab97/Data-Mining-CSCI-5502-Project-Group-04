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

from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.metrics import (confusion_matrix, classification_report, precision_recall_curve, average_precision_score, roc_curve, roc_auc_score) 
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import sklearn


def evenOdd(df, scenario):

  ''' Function to split df even odd where train on even and test on odd rows'''

  y = df.iloc[:, 5] # botnet code is last colum
  x = df.iloc[:, 0:4] # feature are 0-7

  y_train = y.iloc[::2]  # even
  y_test =  y.iloc[1::2]  # odd

  x_train = x.iloc[::2]  # even
  x_test =  x.iloc[1::2]  # odd

  print(y.shape)
  print(x.shape)
  print(y_train.shape)
  print(y_test.shape)
  print(x_train.shape)
  print(x_test.shape)


  lr_clf = LogisticRegression(n_jobs=8,solver='lbfgs', max_iter=5000)

  lr_clf.fit(x_train, y_train)

  lr_clf_predict = lr_clf.predict(x_test)

  lr_clf_cv_score = cross_val_score(lr_clf,x,y,cv=10,scoring='roc_auc')
 

  print("=== Confusion Matrix ===")
  print(confusion_matrix(y_test, lr_clf_predict))

  print('\n')
  print("=== Classification Report ===")
  print(classification_report(y_test, lr_clf_predict))

  print('\n')
  print("=== All AUC Scores ===")
  print(lr_clf_cv_score)
  print('\n')
  print("=== Mean AUC Score ===")
  print("Mean AUC Score - Logistic Regression: ", lr_clf_cv_score.mean())

  fo = open("run/out/results/lr/ctu-{}-scores.txt".format(scenario), 'w')

  fo.write("===File Stats===\n") 
  fo.write("CTU Scenario {}".format(scenario))
  fo.write("Rows: {}\n".format( df.shape[0]))
  fo.write("Column Names: ") 
  columns = " "
  fo.write((columns.join(list(df.columns))))
  fo.write("\n")
  fo.write("Test/Train Strategy: Even rows are train. Odd rows are test\n")
  fo.write("\n\n")

  fo.write("=== Confusion Matrix ===\n")
  fo.write(np.array2string(confusion_matrix(y_test, lr_clf_predict)))
  fo.write("\n\n") 

  fo.write("=== Classification Report ===\n")
  fo.write(classification_report(y_test, lr_clf_predict))

  fo.write("\n\n") 
  fo.write("=== All AUC Scores ===\n")
  fo.write(np.array2string(lr_clf_cv_score))
  fo.write("\n")
  fo.write("=== Mean AUC Score ===\n")
  fo.write("Mean AUC Score - Logistic Regression: \n") 
  fo.write(np.array2string(lr_clf_cv_score.mean()))

  fo.close() 

  # Plot ROC curve
  disp1 = metrics.plot_roc_curve(lr_clf, x_test, y_test)  
  disp1.ax_.set_title('CTU Scenario {} ROC curve'.format(scenario))
  plt.savefig("run/out/results/lr/ctu-{}-roc_curve.png".format(scenario))

  # Plot Precion Recall curve
  disp2 = metrics.plot_precision_recall_curve(lr_clf, x_test, y_test)
  disp2.ax_.set_title('CTU Scenario {} Precision Recall curve'.format(scenario))
  plt.savefig("run/out/results/lr/ctu-{}-precision_recall_curve.png".format(scenario))
