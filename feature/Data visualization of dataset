#Generation of different plots for visualizing the CTU-13 dataset and some data transforming manipulations of pandas dataframe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = "C:/Users/Shiva/Documents/Anusha Assignments/Data Mining Project/1_capture20110810_botcode.csv"
df = pd.read_csv(fileName)

#To get key-value pair of unique items and their counts for plots where "key=name of the item" and "value=count of item"
def getKeyValuePair(attribute1, df):
    df2 = df[attribute1].value_counts()
    df3 = df2.to_dict()
    #print(df3.keys())
    #print(df3.values())
    return df3
dict_Dpot = getKeyValuePair("Dport", df)
print(dict_Dpot)


#To filter the dataframe to get the values when botnet = 1 (there is botnet traffic)
def botnetDataFrame(filename1):
    df = pd.read_csv(fileName)
    filteredDataFrame = df[(df["botnet"] == 1)]
    #print(filteredDataFrame)
    return filteredDataFrame

def noBotnetDataFrame(filename1):
    df = pd.read_csv(fileName)
    filteredDataFrame = df[(df["botnet"] == 0)]
    #print(filteredDataFrame)
    return filteredDataFrame


# To plot piechart
def pieChart(attribute1, df):
    keyValues = getKeyValuePair(attribute1, df)
    name = keyValues.keys()
    values = keyValues.values()
    itemCount = len(keyValues)
    plt.pie(values, labels=name, autopct='%1.2f%%')
    plt.show()

#pieChart1 = pieChart("Dport", df)


# To plot histogram for numerical attributes in dataset
def histogramPlot(attribute1, df, numOfBins):
    col1 = df[attribute1].astype(float)
    val1 = col1.to_numpy()
    plt.hist(val1, bins=numOfBins)
    plt.ylabel("Frequency")
    plt.xlabel(attribute1)
    plt.show()

#hist1 = histogramPlot("Dur", df, 100)


#Scatter Plot to show correlation between attributes and 'botnet'
def scatterPlot(attribute1, attribute2, df):
    col1 = df[attribute1].astype(float)
    z1 = col1.to_numpy()
    col2 = df[attribute2].astype(float)
    z2 = col2.to_numpy()
    scatterPlt = plt.scatter(z1, z2)
    plt.title("Scatter plot - " + attribute1 + "vs" + attribute2)  # title
    plt.xlabel(attribute1)  # x label
    plt.ylabel(attribute2)  # y label
    plt.show()

#botnetDf = botnetDataFrame(fileName)
#noBotnetDf = noBotnetDataFrame(fileName)
#sPlot1 = scatterPlot("SrcBytes", "botnet", noBotnetDf)
