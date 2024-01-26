import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
July = pd.read_csv(r"D:\Capstone_project\dataset_2\202307-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
July['started_at'] = pd.to_datetime(July['started_at'], format='%Y-%m-%d %H:%M:%S')
July['ended_at'] = pd.to_datetime(July['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = July.isnull().sum()
July = July.dropna()

#checking for duplicates
duplicates = July.duplicated().sum()
#print(duplicates) # no duplicates were found

#-------Sorting by members, checking counts for each type------
July.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot7.csv")

#Counting number of times a route is take (from a certain station to a another station)

#Casuals
July_casual = July[July['member_casual'] == 'casual']
July_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file7.csv")

#Annual members

July_member = July[July['member_casual'] == 'member']
July_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files7.csv")

#--------Difference in hours------------

resul3_casual = July[July['member_casual'] == 'casual']
resul3_member = July[July['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution7.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember7.csv")
