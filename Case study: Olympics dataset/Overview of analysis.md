# Analysis

The dataset ![Olympics_data](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Olympics%20dataset/Dataset/files/athlete_events.csv) was uploaded to Excel, so that we could begin the analysis process.

* Quick preview -> ![table_preview](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Olympics%20dataset/Images/Visualizations/Table_preview.png)

* Fields listed -> ![Fields_of_olympic_dataset](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Olympics%20dataset/Images/Visualizations/Fields_of_Table.png)

* The analysis consists on analyzing the data to gain insight on the probabilities earning a medal in a judo competition based on age, weight and height for male athletes.

## Data cleaning

* First step was to check for null values(NA)/blank cells, using conditional formatting and filtering for 'Null(NA)' values, whichever values were found to be Null or blank cells, were removed except for medals field we only removed blank cells as NA represents a value (no medal acquired).

* Second step is to check for duplicate values, and removing all duplicate values.

An expansion of the columns as well as coloring the headers of each field to make things clearer was done.

## Data analysis

* Based on what we're looking for, we filter the 'sex' field for males only (M) and 'sport' for Judo.

* We want to get the probability of winning a medal based on different criteria(height, weight and age), or in other words how many medals do you win given a certain criteria.

1- Height:

    In a new column which we name 'Total medals', the COUNTIFS function is used to count the the cells in the medals field except the ones which have 'NA', we sort first the height column from lowest to highest height (not necessary but more organized), then we apply the COUNTIFS and drag for all possible heights -> ![cfrfrr]()


