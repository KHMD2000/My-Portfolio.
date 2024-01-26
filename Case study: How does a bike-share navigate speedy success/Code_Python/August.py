import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
August = pd.read_csv(r"D:\Capstone_project\dataset_2\202308-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
August['started_at'] = pd.to_datetime(August['started_at'], format='%Y-%m-%d %H:%M:%S')
August['ended_at'] = pd.to_datetime(August['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = August.isnull().sum()
August = August.dropna()

#checking for duplicates
duplicates = August.duplicated().sum()
#print(duplicates) # no duplicates were found

#-------Sorting by members, checking counts for each type-------
August.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot8.csv")


#Counting number of times a route is take (from a certain station to a another station)

#Casuals
August_casual = August[August['member_casual'] == 'casual']
August_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file8.csv")

#Annual members

August_member = August[August['member_casual'] == 'member']
August_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files8.csv")

#-------Difference in hours---------

resul3_casual = August [August['member_casual'] == 'casual']
resul3_member = August[August['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution8.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember8.csv")
