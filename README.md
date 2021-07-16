Data-Mining-CSCI-5502-Project-Group-04
=======

Summer 2021 course Data mining project (CSCI 5502)

As IoT and network related devices keep
increasing at a rapid rate, the attack surface also
increases allowing malicious actors to gain access
to systems and cause damage and/or extort
money for personal gain.
This repository aims to understand a commonly
known type of malware that is associated with
botnet type of cybercrime. This type of malware
normally operates as a command and control on
the network of the infected where the infected
device connects to the central control agent to
receive instructions such as DDoS. This paper
looks closely at the corresponding network
traffic and uses data mining and machine
learning techniques to try and predict whether a
network pattern is likely malicious or benign.
  

DATA
=======

Dataset 1: CTU-13
https://www.stratosphereips.org/datasets-ctu13

Dataset 2: IoT23
https://www.stratosphereips.org/datasets-iot23



TOOLS
=======

## Preprocessing/Formating
- PyPCAPKit for extracting PCAP file: https://pypi.org/project/pypcapkit/
- Netflow: https://pypi.org/project/netflow/
- Scapy - https://scapy.net/

## Machine Learning/Data Analysis
- Scikit-learn for implementing Machine Learning in Python: https://scikit-learn.org/stable/

## Database Storage
- CSV flat files
- hdf5 library: https://www.hdfgroup.org/solutions/hdf5/
## Visualization
- Plotly https://plotly.com/python/
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

As general best practice, for any scripts that write to disk, write to the run directory in the scripts/run folder. This folder should only be consider a temp working space for scripts to write to. If there is data post processing, these should be moved to a more permanent directory.   


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







