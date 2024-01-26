import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
October = pd.read_csv(r"D:\Capstone_project\dataset_2\202310-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
October['started_at'] = pd.to_datetime(October['started_at'], format='%Y-%m-%d %H:%M:%S')
October['ended_at'] = pd.to_datetime(October['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = October.isnull().sum()
October = October.dropna()

#checking for duplicates
duplicates = October.duplicated().sum()
#print(duplicates) # no duplicates were found

#---------Sorting by members, checking counts for each type-------
October.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot10.csv")


#Counting number of times a route is take (from a certain station to a another station)

#Casuals
October_casual = October[October['member_casual'] == 'casual']
October_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file10.csv")

#Annual members

October_member = October[October['member_casual'] == 'member']
October_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files10.csv")

#Difference in hours

resul3_casual = October[October['member_casual'] == 'casual']
resul3_member = October[October['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution10.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember10.csv")
