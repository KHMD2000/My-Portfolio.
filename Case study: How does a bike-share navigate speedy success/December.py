import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
December = pd.read_csv(r"D:\Capstone_project\dataset_2\202312-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
December['started_at'] = pd.to_datetime(December['started_at'], format='%Y-%m-%d %H:%M:%S')
December['ended_at'] = pd.to_datetime(December['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = December.isnull().sum()
December = December.dropna()

#checking for duplicates
duplicates = December.duplicated().sum()
#print(duplicates) # no duplicates were found

#------Sorting by members, checking counts for each type-----
December.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot12.csv")


#Counting number of times a route is take (from a certain station to a another station)

#Casuals
December_casual = December[December['member_casual'] == 'casual']
December_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file12.csv")

#Annual members

December_member = December[December['member_casual'] == 'member']
December_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files12.csv")

#-------Difference in hours----------

resul3_casual = December[December['member_casual'] == 'casual']
resul3_member = December[December['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution12.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember12.csv")
