## Datasets/Files & File naming

In the datsets/files folder, All the csv files present are used as well as the outputted ones from the analysis to be used for the visualizations in tableau.

### 2023**-divvy-tripdata
These files represent the original datasets used for the anlysis for the different months, where the "**" are replaced for the month. for example 202302-divvy-tripdata represents the dataset of bike rides for the month of february. 

### file + number
The folder datasets/files contains different files one of them is the "file" + number (e.g. file3), which represent the dataset filtered for casual members only and the number stands for the month so for instance, file3 = dataset which was filtered for casual members only for the month of march, and so on.

### files + number
The format "files" + number is similar to the one mentioned above but for annual memembers, so for instance, files5 = dataset filtered for annual members for the month of may.

### plot + number
In this case it is the whole dataset, so for example plot7 is the dataset for the month of july.

### timedisribution + number
Represents the dataset filtered for casual members but with added column representing the hour of the ride. for example timedisribution8 = dataset filtered for casuals with the added column for hours in the month of august.

### timedisributionmember + number
Same as timedisribution but filtered for annual members.

### top5_casual
Represent file with the top5 routes taken by casuals across the year.

### top5_member
Represent file with top5 routes taken by annual members across the year.

### total_plots
represents dataset grouped by rideable type of bike and type of member, with their respective total counts.

## Analysis

The analysis starts by importing the original datasets , then checking for validity by looking at the datatypes of the different columns. Doing that, it is found that the data type of 'started_at' and 'ended_at' is incorrect, hence it is changed to datetime format.
![validation](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20&%20Visualizations/data_type.png)
<img src="https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20&%20Visualizations/data_type.png" alt="Example Image">


