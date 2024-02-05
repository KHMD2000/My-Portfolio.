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

## Code scripts
There are 12 python code scripts, each representing the analysis done for each month, each named after the month the analysis is done for except January which is named 'main'. After doing some brief analysis on each script, all files are exported, and then imported in the 'main' script in which all datasets are joined and further analysis can be performed.

## Analysis

### Preliminary investigation

The analysis starts by importing the original datasets , then checking for validity by looking at the datatypes of the different columns. Doing that, it is found that the data type of 'started_at' and 'ended_at' is incorrect, hence it is changed to datetime format.
![validation_data_type](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/data_type.png)

Next step was to check for missing values and duplicates, where missing values found were dropped, and duplicates if there were any would have been dropped but in this case none were found.

![missing_values/duplicates](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/missing_values_duplicates.png)

<span style="color: red">N.B This investigation was performed for all 12 datasets representing each month. </span>

### Main Analysis
The main anlysis is divided into three parts:

Part 1: Determining the most used bikes for each type of member.

Part 2: Determine the top 5 routes taken by each type of member.

Part 3: Determine the distribution of rides for each type of member across the day.

#### Part 1
After the preliminary analysis performed for each month's dataset. The datasets are exported with the name 'plot' + number. They are all imported in the 'main' python script, in which they are all joined together. Then they are grouped by the rideable type of bike and the type of member, to get the number of counts of all bikes used by each type of member and then sorted in descending order.

![code_snippet_february](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/plot_code_snippet.png)

![code_snippet_of_main(january)](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/code_snippet_january.png)

The visualization is a bar chart showing the number of rides for each type of member and bikes as shown: 

![bar_chart_number_of_rides](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/Dashboard_1__1_.png)

#### Part 2
For this part, each dataset has been filtered twice, once for casuals only and another for members only and then exported, where again, they were imported in the 'main' script, where they are all joined. Once all datasets were joined/concatanated, the new dataset was grouped by 'start_station_name' and 'end_station_name' and each combination of these is a 'route', then they were sorted in descending order and filtered for only the top 5 combinations of each. Which were at the end exported as csv files named 'top5_casual' and 'top5_member'.

![code_snippet_march](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/casual_member_filtering_march.png)

The visualization is a scatter plot, where each point is at the  intersection of the start staton and end station with intensity of color and size of point representing how many times(counts) the route was taken as shown:

![scatterplot_of_routes](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/Dashboard_1.png)

#### Part 3
For this part, filtering for members and casuals was done again, but an added column in which the time(hour) of the ride started was inserted, then the datasets were exported as 'timedisribution' and 'timedisributionmember'. These were imported in the 'main' script where they were all joined together and then exported as 'time casual' and 'time_member' which were used as datasets for the visualtizations.

![code_snippet_April](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/code_snippet_time_april.png)

The visualization is a histogram for both casual rides only and annual members only, where in the x-axis we have the time in which the ride started and in the y-axis we have the number of rides as shown:

![Histogram_of_NumberOfRides_vs_time](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/Dashboard_1__2_.png)

* The following are snippets of the joining procedure of all the datasets and how they were grouped and filtered in the 'main script'

1- ![Appending_datasets1](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/Appending_datasets_into_a_list.png)

2- ![Joining_grouping_sorting_and_filtering_datasets1](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/joing_sorting_filtering_datasets1.png)




