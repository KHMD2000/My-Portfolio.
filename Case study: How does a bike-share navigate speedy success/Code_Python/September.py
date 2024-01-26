import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
September = pd.read_csv(r"D:\Capstone_project\dataset_2\202309-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
September['started_at'] = pd.to_datetime(September['started_at'], format='%Y-%m-%d %H:%M:%S')
September['ended_at'] = pd.to_datetime(September['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = September.isnull().sum()
September = September.dropna()

#checking for duplicates
duplicates = September.duplicated().sum()
#print(duplicates) # no duplicates were found

#------Sorting by members, checking counts for each type------
September.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot9.csv")


#Counting number of times a route is take (from a certain station to a another station)

#Casuals
September_casual = September[September['member_casual'] == 'casual']
September_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file9.csv")

#Annual members

September_member = September[September['member_casual'] == 'member']
September_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files9.csv")

#------Difference in hours----------

resul3_casual = September[September['member_casual'] == 'casual']
resul3_member = September[September['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution9.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember9.csv")
