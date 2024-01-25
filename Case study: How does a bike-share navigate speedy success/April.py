import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
April = pd.read_csv(r"D:\Capstone_project\dataset_2\202304-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
April['started_at'] = pd.to_datetime(April['started_at'], format='%Y-%m-%d %H:%M:%S')
April['ended_at'] = pd.to_datetime(April['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = April.isnull().sum()
April = April.dropna()

#checking for duplicates
duplicates = April.duplicated().sum()
#print(duplicates) # no duplicates were found

#----------Sorting by members, checking counts for each type--------
April.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot4.csv")


#-------Counting number of times a route is take (from a certain station to a another station)-------
#Casuals
April_casual = April[April['member_casual'] == 'casual']
April_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file4.csv")

#Annual members

April_member = April[April['member_casual'] == 'member']
April_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files4.csv")

#---------Difference in hours----------

resul3_casual = April[April['member_casual'] == 'casual']
resul3_member = April[April['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution4.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember4.csv")
