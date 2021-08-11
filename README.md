Data-Mining-CSCI-5502-Project-Group-04
 

  
Analysis and detection of malicious events in Network traffic
=======

Group Memebers
======= 
Tim Coleman (colemat@colorado.edu)
Anusha Basavaraja (anba9017@colorado.edu) 
Christopher Bisbee (chbi4702@colorado.edu)

Project Description 
======= 

As the number of IoT and network related devices keeps growing at an exponential rate, security is a major concern among network administrators and companies at large trying to secure the networks and devices from malicious attacks such as ransomware, spyware, DDoS, and other types of attacks.

The goal of our project was to analyze and learn interesting patterns from network traffic that contains known malicious intent in an effort to try and prevent attacks from happening and mitigating loss.

There are published data sets such as CTU-13 which contain netflow network captures that are classified as benign or malicious. Part of the goal for this project would be to build a machine learning model in an attempt to detect malicious events and optimize the balance of false positives to false negative ratios and maximize the true positive detection rate.

Questions to answer? 
=======
- What are the preprocessing tasks that needs to be done to prep the dataset for Data mining task?
- What are the classification techniques used to classify the netflow data into benign and malicious classes?
- How to compare different supervised ML models to detect the botnet traffic?
- What future work can be performed?

Knowledge Gained and Applied
=======
- Using data mining tools such as Pandas, Scipy, Sklearn, Matplotlib
- Interpreting results such Precision, Recall, Sensitivity, Specificity, ROC, AP
- Feature extraction (e.g. correlations)


Presentation and Paper
=======
- [Presentation Video](04_AnalysisAndDetectionOfMaliciousEventsInNetworkTraffic_Part6_Video.mp4)  
- [Presentation Slides](04_AnalysisAndDetectionOfMaliciousEventsInNetworkTraffic_Part6.pdf)  
- [Final Paper](04_AnalysisAndDetectionOfMaliciousEventsInNetworkTraffic_Part4.pdf)

DATA
=======

Dataset 1: CTU-13
https://www.stratosphereips.org/datasets-ctu13


TOOLS
=======

## Preprocessing/Formating
- Netflow: https://pypi.org/project/netflow/
- Scapy - https://scapy.net/

## Machine Learning/Data Analysis
- Scikit-learn: https://scikit-learn.org/stable/
- Sklearn: https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

## Database Storage
- CSV flat files
## Visualization
- Matlab https://matplotlib.org/  


CODE ORGANIZATION
=======

Below is the python code organization for this repo. Python modules should be created and placed in the appropriate subfolder (`preprocess, ml, feature`) and the scripts to run data analysis should be under `scripts`.  

As an example, `preprocess.tranform` is a python module and should be contain collection of methods that are related to transforming the CTU-13 data sets.

The CTU-13-Dataset should be extracted under the root of this repo and follow the format listed below. If you run the command below it will exact the contents in the same manner. 

`tar -xvzf CTU-13-Dataset.tar.gz` 

Message @tijcolem to get the data set, or go to the CTU data set link above for the original copy and format it. 

You can run the simple preprocessing scripts

```
cd scripts 
python3 preprocess-example.py
```


 For any scripts that write to disk, write to the run directory in the scripts/run folder. This folder should only be considered a temp working space for single runs. If there is desired data to be kept post-processing, data should be moved to a more permanent directory.   

 Below represents the code tree

```shell
── CTU-13-Dataset
│   ├── 10_README
│   ├── 10_capture20110818.binetflow
│   ├── 11_README
│   ├── 11_capture20110818-2.binetflow
│   ├── 12_README
│   ├── 12_capture20110819.binetflow
│   ├── 13_README
│   ├── 13_capture20110815-3.binetflow
│   ├── 1_README.html
│   ├── 1_capture20110810.binetflow
│   ├── 2_README
│   ├── 2_capture20110811.binetflow
│   ├── 3_README
│   ├── 3_capture20110812.binetflow
│   ├── 4_README
│   ├── 4_capture20110815.binetflow
│   ├── 5_README
│   ├── 5_capture20110815-2.binetflow
│   ├── 6_README
│   ├── 6_capture20110816.binetflow
│   ├── 7_README
│   ├── 7_capture20110816-2.binetflow
│   ├── 8_README
│   ├── 8_capture20110816-3.binetflow
│   ├── 9_README
│   └── 9_capture20110817.binetflow
├── README.md
├── feature
│   └── __init__.py
├── ml
│   └── __init__.py
├── preprocess
│   ├── __init__.py
│   └── transform.py
├── scripts
│   └── preprocess-example.py
```







