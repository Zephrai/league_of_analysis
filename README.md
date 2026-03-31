## League of Legends Data Analysis

# The Question: 
- How will a player's winrate be effected by claiming the first dragon in the game?

# Hypothesis: 
- I estimate on average, the team that claims the dragon first will have a 5-10% higher probable winrate than
the teams that do not.

# Equipment:
- I will use CSV ranked data of 50,000 League of Legends games from "https://www.kaggle.com/datasets/datasnaek/league-of-legends?resource=download".
- The Pandas library will be used with Python to conduct any Data Analysis.
- Matplotlib to create graphs of the Data.

# Method: 
- The data will be cleaned of all anomalies, anomalies are defined by games that end before an objective is claimed,
data that is corrupted/N/A etc.
- To make sure there is as little statistical bias as possible, I will remove Data where the Games last longer than 35 minutes,
this is because at 35 minutes, the Baron and Elder dragon objective teams can claim will drastically affect the Data, such games should be
treated as anomalies.
- The data will be plot onto a bar chart to easily compare the win percentage of games when either team acquires, or does not acquire
the first dragon of the game.

# Conclusion:
- TBD
After processing and analysing the data, the results show that my hypothesis was not only correct, but it surpasses my estimations
completely, both teams gained a massive 22%~ increase in winrate. This means that getting the first dragon could be one of the biggest
factors in deciding which team will win the game.

Such a large increase would suggest that it is not mere correlation that acquiring the first dragon will lead to a better
likelyhood of winning the game. However, one must consider that the cause and effect of a team taking the dragon
would imply they are already in a position to take it in the first place.

AKA, "A team that is more likely to win the game is also more likely to slay the dragon to begin with."

One way to check this new hypothesis is to filter out the games where the first dragon has been slain with a sizeable "gold lead".
In layman's terms, "gold" in this game equates very strongly to which team is in a "winning position". Therefore, one can remove the games
where there is a large gap between both team's total gold. 
This means, whichever team got the Dragon did so on equal footing, and thus acquiring it was not correlated to that team
already being in a more favourable circumstance.
Unfortunately, the dataset which I have access to does not have this kind of data. So I will not be able to do such analysis.

An interesting case this analysis suggested was that the Blue team, for some unknown reason has a small 
chance of winning a game over the red team. Both with/without the first Dragon,
Blue team's winrate is close to 1%~ greater than red team.

This is an alarmingly high difference, out of 34889 games, Blue team has a 51.2% winrate, and Red team has a 48.9% winrate
The standard error for 34889 games:
S.E = sqrt(0.512 * 0.489) / 34889 = 0.0027 (0.27%)
Margin of error at 95% is 1.96 * 0.27% which is approximately 0.53%
Which means:
Blue winrate is 51.2% ± 0.53%
Red winrate is 48.9% ± 0.53%
The difference is 2.3% between them, 2.3% / 0.53% gives us how many standard deviations they are apart.
2.3 / 0.53 = 4 standard deviations!!!

This analysis proves beyond reasonable doubt that the Blue Team has a much higher probability of winning, regardless of gamestate.
If you're on red side, getting the first dragon is the difference between being at a statistical loss and an outright win.
