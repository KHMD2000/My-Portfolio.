import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.patches import Patch

#importing files
january = pd.read_csv(r"D:\Capstone_project\dataset_2\202301-divvy-tripdata.csv")

#Data validation; checking dataset and various datatypes
print(january.dtypes)

#changing datatype of started_at and ended_at to datetime.
january['started_at'] = pd.to_datetime(january['started_at'], format='%Y-%m-%d %H:%M:%S')
january['ended_at'] = pd.to_datetime(january['ended_at'], format='%Y-%m-%d %H:%M:%S')

#Checking and dropping missing values
missing_values = january.isnull().sum()
january = january.dropna()

#checking for duplicates
duplicates = january.duplicated().sum()
print(duplicates) # no duplicates were found

#------Grouping by members and rideable type, checking counts for each type----

result = january.groupby(['member_casual', 'rideable_type']).size().reset_index(name='counts')


#Counting number of times a route is taken (from a certain station to a another station)

#Casuals
january_casual = january[january['member_casual'] == 'casual']


#Annual members
january_member = january[january['member_casual'] == 'member']

#Creating list of dataframes and concatenating/joining them.
#dfs = list of  dataframes with all casual members.
#dfs2 = list of dataframes with all annual members.
#dfs3 = list of dataframes grouped by type of member and rideable type.
dfs = [january_casual]
dfs2 = [january_member]
dfs3 = [result]
for i in range(2, 13): #reading datasets for the other 11 months and appending them into the list of dataframes
    filename = r"C:\Users\Karem Hesham\PycharmProjects\Cycling\file"+str(i) + '.csv'
    filename2 = r"C:\Users\Karem Hesham\PycharmProjects\Cycling\files"+str(i) + '.csv'
    filename3 =  r"C:\Users\Karem Hesham\PycharmProjects\Cycling\plot"+str(i) + '.csv'
    df = pd.read_csv(filename)
    df2 = pd.read_csv(filename2)
    df3 = pd.read_csv(filename3)
    dfs.append(df)
    dfs2.append(df2)
    dfs3.append(df3)
result_df = pd.concat(dfs, ignore_index=True)#joining tables of all 12 months
grouped_df1 = result_df.groupby(['start_station_name', 'end_station_name']).size().reset_index(name='count')
sorted_df1 = grouped_df1.sort_values(by='count', ascending=False) #sorting by counts in descending order
top_5_combinations_casual1 = sorted_df1.head(5) #filtering for top5 combinations
print(top_5_combinations_casual1)
top_5_combinations_casual1.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\top5_casual.csv")#exporting file

result2_df = pd.concat(dfs2, ignore_index=True)
grouped_df2 = result2_df.groupby(['start_station_name', 'end_station_name']).size().reset_index(name='count')
sorted_df2 = grouped_df2.sort_values(by='count', ascending=False)
top_5_combinations_member1 = sorted_df2.head(5)
print(top_5_combinations_member1)
top_5_combinations_member1.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\top5_member.csv")

result3_df = pd.concat(dfs3,ignore_index = True)
result3_df_grouped = result3_df.groupby(['member_casual', 'rideable_type']).size().reset_index(name='counts')
print(result3_df_grouped.info())
result3_df_grouped.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\total_plots.csv")

#-----Difference in hours-------
#checking for distribution of rides as a function of time
#dfs4, dfs5 = dfs, dfs2 but with added column for the hour
resul3_casual = january[january['member_casual'] == 'casual']
resul3_member = january[january['member_casual'] == 'member']
resul3_casual['hour'] = resul3_casual['started_at'].dt.hour
resul3_member['hour'] = resul3_member['started_at'].dt.hour

dfs4 = [resul3_casual]
dfs5 = [resul3_member]
for i in range(2, 13):
    filename4 = r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisribution"+str(i) + '.csv'
    filename5 = r"C:\Users\Karem Hesham\PycharmProjects\Cycling\timedisributionmember"+str(i) + '.csv'
    df4 = pd.read_csv(filename4)
    df5 = pd.read_csv(filename5)
    dfs4.append(df4)
    dfs5.append(df5)
total_casual = pd.concat(dfs4,ignore_index=True)
total_casual.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\time_casual.csv")
total_member = pd.concat(dfs5,ignore_index=True)
total_member.to_csv(r"C:\Users\Karem Hesham\PycharmProjects\Cycling\time_member.csv")
