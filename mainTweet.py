import pandas
from hdfs import InsecureClient
import os
from csv import reader
import numpy as np
from plotGraphTw import plotGraph

client_hdfs = InsecureClient('http://localhost:50070')

with client_hdfs.read('/user/sentimentAnly.csv') as read_data:
    df = pandas.read_csv(read_data)
positive = {'trump':[],'modi':[],'gandhi':[]}
negative = {'trump':[],'modi':[],'gandhi':[]}
neutral = {'trump':[],'modi':[],'gandhi':[]}
for row in df.to_records():
    print(row)
    if row[2]=='Narendra Modi':
        positive['modi'].append(row[3])
        negative['modi'].append(row[4])
        neutral['modi'].append(row[5])

    elif row[2] == 'Rajiv Gandhi':
        positive['gandhi'].append(row[3])
        negative['gandhi'].append(row[4])
        neutral['gandhi'].append(row[5])
    else:
        positive['trump'].append(row[3])
        negative['trump'].append(row[4])
        neutral['trump'].append(row[5])
ps_avg = []
ps_avg.append(np.array(positive['trump']).mean())
ps_avg.append(np.array(positive['modi']).mean())
ps_avg.append(np.array(positive['gandhi']).mean())
print(positive['trump'])
print(ps_avg)

ng_avg = []
ng_avg.append(np.array(negative['trump']).mean())
ng_avg.append(np.array(negative['modi']).mean())
ng_avg.append(np.array(negative['gandhi']).mean())
print(ng_avg)

nt_avg = []
nt_avg.append(np.array(neutral['trump']).mean())
nt_avg.append(np.array(neutral['modi']).mean())
nt_avg.append(np.array(neutral['gandhi']).mean())
print(nt_avg)
plotGraph(ps_avg,ng_avg,nt_avg)
