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

4-  Analyze: Sorting and filtering data in a way to gain insights. In this analysis I focused on three things:

    1- Calculating probability HTR = FTR.

    2- Calculating probability of all possible cominations of HTR and FTR.

    3- Calculating the probabilities of the outcomes given that FTR = HTR or FTR ≠ HTR.

5-  Share: Using the insgihts gained in the analysis process, visualizations were created to be shared in my report.

* Visulizations
