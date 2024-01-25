import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
March = pd.read_csv(r"D:\Capstone_project\dataset_2\202303-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
#print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
March['started_at'] = pd.to_datetime(March['started_at'], format='%Y-%m-%d %H:%M:%S')
March['ended_at'] = pd.to_datetime(March['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = March.isnull().sum()
March = March.dropna()

#checking for duplicates
duplicates = March.duplicated().sum()
#print(duplicates) # no duplicates were found

#-------Sorting by members, checking counts for each type---------
March.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot3.csv")



#-------Filtering for casuals/members and exporting to csv file------
#Casuals

March_casual = March[March['member_casual'] == 'casual']
March_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file3.csv")


#Annual members

March_member = March[March['member_casual'] == 'member']
March_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files3.csv")



#-----------Difference in hours----------
#checking for distribution of rides as a function of time and exporting to external csv file
resul3_casual = March[March['member_casual'] == 'casual']
resul3_member = March[March['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour
resul3_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution3.csv")
resul3_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember3.csv")
