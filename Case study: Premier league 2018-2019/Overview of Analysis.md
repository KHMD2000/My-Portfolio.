# Analysis

The dataset ![premier-league-2018/2019](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Dataset/files/soccer18-19.csv) was uploaded into big query so that analysis could be performed using SQL.

From a quick preview of the table as shown here -> ![Table-preview](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/preview_table.png)

We can see that the dataset is formed of the following fields: ![table_fields](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/Fields_of_Table.png)

The analysis consists in understanding the relations between the half time result of a game and the full time result, based on that, the first query was to check the probability of getting the same outcome at half time and full time (for example if home team(H) is winning at halftime, we check probability that it won also at full time and so on).

First query -> ![probability-HTR=FTR](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/prob_FTR_HTR.png)

From this we get that the probability of getting same result at Half time and Full time is 0.6 or 60%.

The second query was to check all the possible combinations of outcomes (for example H-A, means home team was winning at half time and away team won at full time); hence the 'second query' is multiple queries checking for different combinations probabilities, so I'll show one of the combinations queried (they should be 9: H-H,A-A,H-A,A-H,H-D,D-H,A-D,D-A and D-D).

Second query -> [snippet-Halftime=H/Fulltime=A](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR_H_FTR_A.png)

Doing this, we get the possibilities of all possible combinations

