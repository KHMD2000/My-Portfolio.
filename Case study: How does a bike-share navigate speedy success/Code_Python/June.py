import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
June = pd.read_csv(r"D:\Capstone_project\dataset_2\202306-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
June['started_at'] = pd.to_datetime(June['started_at'], format='%Y-%m-%d %H:%M:%S')
June['ended_at'] = pd.to_datetime(June['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = June.isnull().sum()
June = June.dropna()

#checking for duplicates
duplicates = June.duplicated().sum()
#print(duplicates) # no duplicates were found

#------Sorting by members, checking counts for each type------
June.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot6.csv")


#------Counting number of times a route is take (from a certain station to a another station)-----
#Casuals
June_casual = June[June['member_casual'] == 'casual']
June_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file6.csv")

#Annual members

June_member = June[June['member_casual'] == 'member']
June_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files6.csv")

#-----------Difference in hours----------

resul3_casual = June[June['member_casual'] == 'casual']
resul3_member = June[June['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution6.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember6.csv")
