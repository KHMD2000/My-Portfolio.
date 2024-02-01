# Premier league games 2018-2019 analysis using SQL/R Language

## Scenario

A local soccer team has recently signed some junior players and wants to give them as much experience as possible without losing games, if the coach could be confident in the outcome of the game by halftime, they would be more likely to give the junior players more time on the field.

My task is to check if I can estimate the outcome of a game based on the halftime results.

## Data Analysis Process

The data analysis process used is the following:

1- Ask:

    1- what are the probabilities of all the possible combinations of Half-time results(HTR) and Full-Time results(FTR).

    2- Given that FTR = HTR what are the probabilities of the different outcomes.

    3- Given that FTR ≠ HTR what are the probabilities of the different outcomes.

2- Prepare: The dataset has been collected from ![dataset_source](https://data.world/chas/2018-2019-premier-league-matches), which is a public dataset availiable to anyone containing the data from the Premier league season 2018-2019 matches.

3- Process: Cleaning, transforming and organizing the raw data to make it suitable for analysis. Handling of missing values, addressing outliers, and performing any necessary data manipulations to ensure data is in a usable form for subsequent analytical steps.

4-  Analyze: Sorting and filtering data in a way to gain insights. In this analysis I focused on Four things:

    1- Calculating probability HTR = FTR.

    2- Calculating probability of all possible cominations of HTR and FTR.

    3- Calculating the probabilities of the outcomes given that FTR = HTR or FTR ≠ HTR.

    4- Calculating probabilities of fdifferent outcomes given knowledge of HTR.

5-  Share: Using the insgihts gained in the analysis process, visualizations were created to be shared in my report.

* Visulizations:

    1-  Pie chart showing probabilities of all possible combinations -> ![All_possible_combinations_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/combinations_of_HTR-FTR.png)

    2- Pie chart showing probabilities of the three availiable combinations where HTR = FTR -> ![HTR=FTR_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/FTR_HTR.png)

    3- Pie chart showing probabilities of the 6 availiable combinations where HTR ≠ FTR -> ![HTR≠FTR_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/FTR___HTR.png)

    4-  Pie chart showing probabilities of the possible combinations given HTR = H -> ![HTR=H_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___H_pie_chart.png)

    5- Pie chart showing probabilities of the possible combinations given HTR = A -> ![HTR=A_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___A_pie_chart.png)

    6- Pie chart showing probabilities of the possible combinations given HTR = D -> ![HTR=D_pie_chart](https://gitlab.com/computational1/my_portfolio/-/blob/main/Case%20study:%20Premier%20league%202018-2019/Images/visualizations/HTR___D_pie_chart.png)


* Insights:

    1- From the first visualization we can observe that the highest possible outcome is the H-H or in other words that at HTR = FTR = Home team winning, and the least probable result is the H-A which is home team winning at HT and Away team grabbing the win at FT, we can also observe that probability of H-D is also very small standing at 4.2%, which makes it relatively likely that given that home team is winning at HT it will also win at FT.

    2- The second visualization shows that between the possible equal results of both half (HT and FT), the H-H is the one most likely while the D-D is the least likely. From which we could infer that given that the Home team is winning, there is a good chance it is going to win at the end and given that at Half time, the teams are drawing, the final result may be the most susceptible to change, but further insights can be only gained by looking at probabilities of Full time result given the knowledge of the Half time result.

    3- The third visualization proves more the susceptibility in the final result based on a draw at half time, where the two most probable outcomes when HTR ≠ FTR is D-H and D-A, which makes it tricky on weather to sub-in junior players during the course of the game or not if the teams are drawing at half time.

    4- The fourth visualization shows that given that at Half-time the home team is winning there is a big likelihood of it winning at full time as well with a probability of 84.1%, and a very small chance of losing standing at 3.2%, which suggests that subbing in a junior player for the home team is a good idea as either way there is a large likelihood that it won't impact the result that much, and the same goes for the away team, subbing in a junior player will give them a chance to grow, and since the outcome of the game is predominantly leaning towards the winning of the home team, subbing in a junior player might give a breath of fresh air and maybe change the outcome of the game.

    5- The fifth visualization similar to the fourth one, sees a predominant probability that given that at Half-time the away team is winning, it will also win at full time, hence suggesting that subbing in junior players might be the way to go for them. For the home team it is the same using the same argument from the previous visualization, although the probability of home team winning is a bit higher (12.3% vs 3.2%), I still believe that is sufficiently low to warrant the subbing in of junior players.

    6- The sixth visualization confirms yet again the susceptibility in the outcome when teams are drawing at half time, In this case it could go whichever way, hence it would be better to keep the experienced/best players in the team's roaster in the field.

 * Act: Recommendations based on the insights:

    1- Sub in junior players when the probability of the game going in a certain direction is relatively high(applies for both if it the home team or away team); based on the analysis this occurs when at Half time home team is winning and also when Away team is winning.

    2- Do not sub in junior players when game could go either way, high unpredictability; this occurs when teams are drawing at Half time.


Addendum:

More data would be required to make a better analysis, for example the results of the game during the various phases of the second half, so that for example if at half time there was a draw but at the 70th minute home team is winning by 3-1, subbing in junior players would be a good idea.






