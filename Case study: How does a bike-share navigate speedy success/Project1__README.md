# Cyclistic bike-share data analysis using python/tableau

## Scenario

The director of marketing of a fictional bike-share company in Chicago believes the company's future success depends on maximizing the number of annual memberships. Therefore, an understanding of the difference between casual members and annual members in their usage of Cyclistic bikes. From these insights, a new marketing strategy will be designed to convert casual riders into annual members.

## Data analysis process

The data analysis process used is the following:

1- Ask: 

        How do annual members and casual riders use Cyclistic bikes differently?

        Why would casual riders buy Cyclistic annual memberships?

        How can Cyclistic use digital media to influence casual riders to become members?
        
2- Prepare: Usage of Cyclistic’s historical trip data to analyze and identify trends. Data of previous 12 months was used: [Datasets_used](https://divvy-tripdata.s3.amazonaws.com/index.html)(Note: The datasets have a different name because Cyclistic
is a fictional company. For the purposes of this case study, the datasets are appropriate and
will enable me to answer the business questions. The data has been made available by
Motivate International Inc. under this [license](https://divvybikes.com/data-license-agreement).)

3- Process: Cleaning, transforming and organizing the raw data to make it suitable for analysis. Handling of missing values, addressing outliers, and performing any necessary data manipulations to ensure data is in a usable form for subsequent analytical steps.

4- Analyze: Sorting and filtering data in a way to gain insights. In this analysis I focused on three things:

    1- The prefered type of bike each type (annual member/casual) used.

    2- The preffered routes by each type.

    3- The time of the day each type uses the bikes most.

From these things, we can gain insight into the differences between the casual and annual members.

5- Share: Using the insgihts gained in the analysis process, visualizations were created to be shared in my report.

* Visualizations:

1- ![bar_chart_number_of_rides](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/Dashboard_1__1_.png)

2- ![scatterplot_of_routes](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/Dashboard_1.png)

3- ![Histogram_of_NumberOfRides_vs_time](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20How%20does%20a%20bike-share%20navigate%20speedy%20success/Images%20%26%20Visualizations/Dashboard_1__2_.png)

* Insights

    1- From the first plot we observe that Annual members have much more rides than The casual members, in fact almost the double. But the distribution of rides between the classic and electric type of bikes is fairly similar, where for casual members classic bikes are used a bit less than double the times of electric bikes and for annual members is pretty much the same. A major difference is in the usage of docked bikes, Annual members register no usage of docked bikes while casual members do, although a much lower number of rides compared to the casual and electric bikes.

    2- From the second plot, we observe that top 5 used routes for the two types of members are completely different. However, the most relevant thing to observe is the spread of the rides for the two types; for the annual members the number of rides for the top 5 routes are pretty much the same, but for the casuals it is much less similar where there is a differece of more than 5000 rides between the most used route and the fifth most used route, while for annual members only a difference of 300 rides, and it is easy to see that the trend continues to the next most used routes as well based on the knowledge gained from the first plot about the total number of rides(since number of rides for casuals are much lower than the number of rides of annual members)

    3- From the third plot, we observe the distribution of rides across the day, we can see that they are similar to each other, where the peak rides occur in the interval ranging from 16 to 18 (4 pm to 6 pm), both distributions are skewed to the left, but more for casual members. A relativeky big difference between the two is the higher number of rides in the intervals 6 to 8 and 8 to 10 for annual members, which may be due to annual members using the bikes to commute to their jobs, which typically starts at these hours.

6- Act: Recommendation for designing marketing strategy & other measures to convert casuals to annual members:

    1- Based on the first plot, I would suggest increasing the number of docked bikes stations.

    2- Based on the second plot, I would increase the overall number of stations and bikes on the top 5 routes for casuals, and even more so docked type of bikes, and any type of advertisement to placed along these routes(emphasizing the availiability of not only electric and classic bikes but docked types as well).

    3- Based on the third plot, I would build an advertising campaign showing how refreshing and relaxing is to ride in the afternoon, maybe before sunset by a bit, for example a tv ad where someone rides along a road towards the sunset or an ad attached to a bus which takes the routes most used by casuals.
