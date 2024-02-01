# Analysis

The dataset ![premier-league-2018/2019](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Dataset/files/soccer18-19.csv) was uploaded into big query so that analysis could be performed using SQL.

From a quick preview of the table as shown here -> ![Table-preview](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/preview_table.png)

We can see that the dataset is formed of the following fields: ![table_fields](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/Fields_of_Table.png)

* The analysis consists in understanding the relations between the half time result of a game and the full time result, based on that, the first query was to check the probability of getting the same outcome at half time and full time (for example if home team(H) is winning at halftime, we check probability that it won also at full time and so on).

First query -> ![probability-HTR=FTR](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/prob_FTR_HTR.png)

From this we get that the probability of getting same result at Half time and Full time is 0.6 or 60%.

* The second query was to check all the possible combinations of outcomes (for example H-A, means home team was winning at half time and away team won at full time); hence the 'second query' is multiple queries checking for different combinations probabilities, so I'll show one of the combinations queried (they should be 9: H-H,A-A,H-A,A-H,H-D,D-H,A-D,D-A and D-D).

Second query -> ![snippet-Halftime=H/Fulltime=A](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR_H_FTR_A.png)

Doing this, we get the probabilities of all possible combinations.

* The third and fourth queries where to get further insight on the relations between HTR and FTR where for the third, given that the HTR and FTR were equal what were the probabilities of getting D-D,A-A and H-H; while the fourth given that FTR ≠ HTR, what were the probabilities of the other 6 combinations.

Third query -> ![snippet-HTR=FTR=H](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR_FTR_H.png)

Fourth query -> ![snippet-HTR≠FTR,HTR=H-FTR=D](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR_FTR_HTR_H_FTR_D.png)

THe last triplet of queries (arguably the ones which give the most insights), consider the probability of getting a FTR given the knowledge of the HTR (for example given HTR = H, what are the probabilities of getting H,D and A as a Full time result)

Fifth query(HTR = H) -> ![snippet-HTR=H](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___H.png)

Sixth query(HTR = D) -> ![snippet-HTR=D](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___D.png)

Seventh query(HTR = A) -> ![snippet-HTR=A](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___A.png)

* Based on the results acquired from these queries pie charts to show the probabilities of the different combinations were done using R language.

Snippet pie chart code -> ![R-code,snippet](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/Snippet-R-code.png)

Six visualization were created:

1- Pie chart showing probabilities of all possible combinations -> ![All_possible_combinations_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/combinations_of_HTR-FTR.png)

2- Pie chart showing probabilities of the three availiable combinations where HTR = FTR -> ![HTR=FTR_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/FTR_HTR.png)

3- Pie chart showing probabilities of the 6 availiable combinations where HTR ≠ FTR -> ![HTR≠FTR_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/FTR___HTR.png)

4-  Pie chart showing probabilities of the possible combinations given HTR = H -> ![HTR=H_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___H_pie_chart.png)

5- Pie chart showing probabilities of the possible combinations given HTR = A -> ![HTR=A_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___A_pie_chart.png)

6- Pie chart showing probabilities of the possible combinations given HTR = D -> ![HTR=D_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___D_pie_chart.png)

