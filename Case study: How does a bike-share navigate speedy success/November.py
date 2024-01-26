import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
November = pd.read_csv(r"D:\Capstone_project\dataset_2\202311-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
November['started_at'] = pd.to_datetime(November['started_at'], format='%Y-%m-%d %H:%M:%S')
November['ended_at'] = pd.to_datetime(November['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = November.isnull().sum()
November = November.dropna()

#checking for duplicates
duplicates = November.duplicated().sum()
#print(duplicates) # no duplicates were found

#------Sorting by members, checking counts for each type-------
November.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot11.csv")


#Counting number of times a route is take (from a certain station to a another station)

#Casuals
November_casual = November[November['member_casual'] == 'casual']
November_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file11.csv")

#Annual members

November_member = November[November['member_casual'] == 'member']
November_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files11.csv")

#--------Difference in hours------------

resul3_casual = November[November['member_casual'] == 'casual']
resul3_member = November[November['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution11.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember11.csv")
