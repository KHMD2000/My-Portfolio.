import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
february = pd.read_csv(r"D:\Capstone_project\dataset_2\202302-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
print(february.dtypes)

#changing datatype of started_at and ended_at to datetime.
february['started_at'] = pd.to_datetime(february['started_at'], format='%Y-%m-%d %H:%M:%S')
february['ended_at'] = pd.to_datetime(february['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = february.isnull().sum()
february = february.dropna()

#checking for duplicates
duplicates = february.duplicated().sum()
print(duplicates) # no duplicates were found

#---------Sorting by members, checking counts for each type-------

february.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot2.csv")


#------Counting number of times a route is take (from a certain station to a another station)------

#Casuals

february_casual = february[february['member_casual'] == 'casual']
february_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file2.csv")

#Annual members

february_member = february[february['member_casual'] == 'member']
february_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files2.csv")


#-------Difference in hours--------
#checking for distribution of rides as a function of time
resul3_casual = february[february['member_casual'] == 'casual']
resul3_member = february[february['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour

resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution2.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember2.csv")
