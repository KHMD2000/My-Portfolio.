import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
May = pd.read_csv(r"D:\Capstone_project\dataset_2\202305-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
May['started_at'] = pd.to_datetime(May['started_at'], format='%Y-%m-%d %H:%M:%S')
May['ended_at'] = pd.to_datetime(May['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = May.isnull().sum()
May = May.dropna()

#checking for duplicates
duplicates = May.duplicated().sum()
#print(duplicates) # no duplicates were found

#-----------Sorting by members, checking counts for each type-----------
May.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot5.csv")


#Counting number of times a route is take (from a certain station to a another station)
#Casuals

May_casual = May[May['member_casual'] == 'casual']
May_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file5.csv")

#Annual members

May_member = May[May['member_casual'] == 'member']
May_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files5.csv")

#-----------Difference in hours-------------

resul3_casual = May[May['member_casual'] == 'casual']
resul3_member = May[May['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution5.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember5.csv")
