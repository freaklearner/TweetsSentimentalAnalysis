from csv import writer
import os
from os import path
import pandas
from hdfs import InsecureClient


def writetweetsdata(time,leader,list):
    client_hdfs = InsecureClient('http://localhost:50070')
    #print(temp)
    #df = pandas.DataFrame(data = {'time':[time],'leader':[leader],'positive':[list[0]],'negative':[list[1]],'neutral':[list[2]]})
    #print(df)
    with client_hdfs.write('/user/sentimentAnly.csv',encoding='utf-8',overwrite=False,append=True) as writer_csv:
        csv_writer = writer(writer_csv)
        csv_writer.writerow([time,leader,list[0],list[1],list[2]])
        #df.to_csv(writer)
    #    csv_writer = writer(file)
    #    csv_writer.writerow([time,leader,list[0],list[1],list[2]])
#print("SuccessFul Run.....")
