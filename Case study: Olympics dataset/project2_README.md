# Olympic games from Athens 1896 to Rio2016 Analysis using Excel

## Scenario

An international Judo club is looking for new ways to leverage data for competition. One idea they have had is to use past competition data to estimate the threat of future opponents. They have provided  a dataset of past Olympic data and want to know whether usage of information such as the height, weight and age of a judo competito is possible to estimate the probability that they will earn a medal.

## Data Analysis Process

The data analysis process used is the following:

1- Ask:

    1- What is the probability of a judo athlete to win a medal based on height ?

    2- What is the probability of a judo athlete to win a medal based on weight ?

    3- What is the probability of a judo player to win a medal based on age ?

2- Prepare: The data set has been collected from [dataset_suource](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) which is a consolidated version of data from [original_unconsolidated_source](https://www.sports-reference.com/) under the following [license](https://creativecommons.org/publicdomain/zero/1.0/)

3- Process: Cleaning, transforming and organizing the raw data to make it suitable for analysis. Handling of missing values, addressing outliers, and performing any necessary data manipulations to ensure data is in a usable form for subsequent analytical steps.

4- Analyze: Sorting and filtering data in a way to gain insights. In this analysis I focused on three things:

    1- Getting insight on the relation between height and number of medal acquired.

    2- Determining the reation between weight and number of medals obtained.

    3- Investigating the relation between age and number of medals gained.

5-  Share: Using the insgihts gained in the analysis process, visualizations were created to be shared in my report.

* Visualizations

    1- Scatter plot of the number of medals obtained versus height of Judo athlete -> ![scatter_height](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Total_number_of_medals_vs_height.png)

    2- Pie chart for probabilities of winning a medal based on height of Judo athlete -> ![pie_chart_height](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/probability_of_winning_medals_based_on_height.png)

    3- Scatter plot of the number of medals obtained versus age of Judo athlete -> ![scatter_age](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/total_number_of_medals_vs_age.png)

    4- Pie chart for probabilities of winning a medal based on age of Judo athlete -> ![pie_chart_age](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/probability_of_winning_medals_based_on_age.png)

    5- Scatter plot of the number of medals obtained versus weight of Judo athlete -> ![scatter_weight](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/total_number_of_medals_vs_weight.png)

    6- Pie chart for probabilities of winning a medal based on weight of Judo athlete -> ![pie_chart_weight](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/probability_of_winning_medals_based_on_weight.png)

* Insights:

    1- From first scatter plot for the height, we see that it takes a gaussian shape where the number of medals obtained increase with increasing height till it reaches a peak at 179 cm and then decreases again.

    2- From the pie chart we confirm the results from the scatter plot, where the highest probability to win a medal falls in the interval 176cm to 180cm at 18 % and decreases as we go at lower or higher heights.

    3- From the scatter plot for the age, we oberve that the distribution is similar to the height but a bit more right skewed, where the number of medals obtained increase with age untill it reaches a peak at 23 years and the decreases.

    4- From the pie chart we observe that highest probability of winning a medal occurs at the ages 22-24 at 27 % and a close second is for the ages 25-27 at 24%, which makes sense from the values observed from the scatter plot.

    5- From the scatter plot for the weight, we observe a bit of a different behavior where the initial increase in the number of medals as the independent variable increases (in this case weight) is not 'linear'(linear in the sense that they increase together, maybe a more fitting word is proportional), but rather there are fluctuations where it inccreases and decreases and the overall distribution is heavily skewed to the right, the distribution reaches a peak at 70 kg weight, and then decreases untill it pretty much plateaus at weighgt of 106 kg with small bumps after it.

    6- From the pie chart we observe two intervals which dominate over all others which are the 71-80 at 29% and the 61-70 at 28%, their combined share accounts for more than half of the total medals obtained.

* Act: Recommendations based on insights:

    1- Judo players falling the height interval between 176cm and 180cm have highest probability of winning a medal, invest resources on these athletes and for the future look for athletes falling in this height interval.

    2- Judo players falling in the age interval 22-24 have highest probability of winning a medal, Investment of resources on these athletes, as it seems they reach their peak potential at this age interval.

    3- Judo players falling in the weight interval between 61 and 80, are the most probable to win a medal, hence I recommend adjustment of a diet(based on the height of the athlete as well), to reach this interval of weight.

