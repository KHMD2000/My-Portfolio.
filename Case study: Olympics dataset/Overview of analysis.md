# Analysis

The dataset [Olympics_data](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Dataset/files/athlete_events.csv) was uploaded to Excel, so that we could begin the analysis process.

* Quick preview -> ![table_preview](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Table_preview.png)

* Fields listed -> ![Fields_of_olympic_dataset](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Fields_of_Table.png)

* The analysis consists on analyzing the data to gain insight on the probabilities earning a medal in a judo competition based on age, weight and height for male athletes.

## Data cleaning

* First step was to check for null values(NA)/blank cells, using conditional formatting and filtering for 'Null(NA)' values, whichever values were found to be Null or blank cells, were removed except for medals field we only removed blank cells as NA represents a value (no medal acquired).

* Second step is to check for duplicate values, and removing all duplicate values.

An expansion of the columns as well as coloring the headers of each field to make things clearer was done.

## Data analysis

* Based on what we're looking for, we filter the 'sex' field for males only (M) and 'sport' for Judo.

* We want to get the probability of winning a medal based on different criteria(height, weight and age), or in other words how many medals do you win given a certain criteria.

### 1- Height:

In a new column which we name 'Total medals', the COUNTIFS function is used to count the the cells in the medals field except the ones which have 'NA', we sort first the height column from lowest to highest height (not necessary but more organized), then we apply the COUNTIFS and drag for all possible heights -> 
![total_medals_based_on_height](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Total_medals_height.png)

There are multiple repeated values, as there are multiple people with same height, or same person who competed more than once, hence a new field created and named 'Total medals_to_draw' which has the unique value of counts and another field named 'Height_to_draw' which has all height values paired with the corresponding number of counts, as shown ->
![total_medals_to_draw-&-height_to_draw](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/total_medals_height.png)

Using these two fields a scatter plot was done with height in the x-axis and the medals won in the y-axis as shown here ->
![scatter_plot_height](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Total_number_of_medals_vs_height.png)

But since we want to get probabilities two new fields were created which were named 'Interval_5_height' and 'percentage won', the first field has for each cell 5 values for the height (e.g. 156-160), and the percentage of medals won, which is given by the sum of medals won by that height interval divided by the sum of all medals multiplied by 100 as shown here ->
![interval_5_height-&-percentage_won](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Interval5_height.png)

Using these values a pie chart was drawn as shown here -> 
![pie_chart_height](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/probability_of_winning_medals_based_on_height.png)

### 2- Age:

Same procedure was done for age where we first sort age from youngest to oldest, then  a new field was created named "Total_medals_age" then applied COUNTIFS function and dragging for all possible ages to get the total number of medals acquired for Judo athletes of a specific age as shown ->
![total_medals_age](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Total_medals_age.png)

Then two fields were created named 'Age_to_draw' and 'medals_age_to_draw' which represent the same fields 'total medals_to_draw' and 'Height_to draw' but for age ->
![total_medals_to_draw-&-age_to_draw](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Age_vs_medals.png)

A scatter plot was created using the values from these two fields where the age is in the x-axis while the number of medals is on the y-axis ->
![age_vs_medalscounts_plot](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/total_number_of_medals_vs_age.png)

To get the probabilities, we create two fields named 'Interval_3_age' and 'percentage_won_age', percentage won is calculated the same way as in the height, and in this case instead of taking an interval of 5 values, 3 were taken (e.g 22-24, all inclusive) ->
![Interval_3_age_vs_percentage_won](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Interval_3_age_vspercentage_won.png)

A pie chart was created using the values from these two fields ->
![pie_chart_age](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/probability_of_winning_medals_based_on_age.png)

### 3- Weight:

Same procedures yet again are applied for weight, where I sort from the lightest to the heaviest, then a new field was created named 'Total_medals_weight' then applied COUNTIFS function and dragging for all possible wieghts to get the total number of medals acquired for Judo athletes of a specific weight as shown ->
![total_medals_weight](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/total_medals_weight.png)

Then two fields were created named 'Weight_to_draw' and 'medals_weight_to_draw' which represent the same fields as the ones discussed in height and age ->
![total_medals_to_draw-&-weight_to_draw](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Weight_vs_medals.png)

A scatter plot was created using the values from these two fields where the weight is in the x-axis while the number of medals is on the y-axis -> 
![weight_vs_medalscounts](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/total_number_of_medals_vs_weight.png)

To get the probabilities, we create two fields named 'Interval_10_weight' and 'percentage_won_weight', percentage won is calculated in the same manner as in height and age, while in this case Interval is taken for 10 values in each cell (e.g. 56kg to 65kg) ->
![Interval_10_weight_vs_percentage_won](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/Interval_10_weight_vs_percentagewon.png)

A pie chart was created using the values from these two fields ->
![pie_chart_weight](https://github.com/KHMD2000/My-Portfolio./blob/main/Case%20study%3A%20Olympics%20dataset/Images/Visualizations/probability_of_winning_medals_based_on_weight.png)
