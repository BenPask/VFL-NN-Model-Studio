# VFL NN Model Studio

VFL Neural Network Studio is a website where users can create, train, visualize, and analyze custom neural networks to predict the VALORANT Fantasy League (VFL) scores of professional VALORANT players. Built around a zero-dependency vanilla JavaScript engine developed specifically for this project. The engine features linear algebra/matrix math utilities, selectable model architecture types, model training from .csv or .json data, as well as a PRNG function (for weight initialization) and a custom scatterplot graphing module that returns an HTML canvas element. The training data was collected from an API for vlr.gg, a popular stats/news resource in the VALORANT esports space.

VALORANT Fantasy League (VFL) Player Score Prediction Tool

# Model Info

On VFL Neural Network Model Studio, users create, train, and visualize a regression-based neural network prediction model using an HTML-based selection interface that sends information to predict VFL points, a cumulative metric created by the VALORANT Fantasy League developers to reflect strong player performance. We selected and created the features for potential models based on the VFL scoring rules found [here]([url](https://www.valorantfantasyleague.net/rules)). For a full list of the features used and explanations of their meaning and relevance to the project, please scroll to the "Feature List" section of this file.

# Feature List:

### PLAYER BASED FEATURES:

**KPR_RECENT** - _"Kills per round recent"_ - averages a player's kills/round in their last tournament/stage showing. Accounts for many of VFL's scoring rules that emphasize player kills and general performance.

**KPR_CAREER** - _"Kills per round career"_ - averages a player's kills/round during their whole career. Attempts to account for consistency in player kill stats over longer periods of time.

**VLR_RATING_RECENT** - _"Vlr.gg rating recent"_ - is a player's VLR rating from the most recent tournament/stage. Accounts for VFL scoring's various bonus points awarded to players with high VLR ratings and top-placing VLR ratings in a given tournament. We chose VLR rating over the various stats that contribute to VLR's rating because we wanted to account for VFL scoring's emphasis on kills and VLR rating individually.

**VLR_RATING_CAREER** - _"Vlr.gg rating career"_ - is a player's average VLR rating during their whole career. Attempts to account for consistency in VLR ratings over a longer period of time.

**MK_MAP_RECENT** - "Multi-kill map recently" - averages a player's number of multi-kills per map over the latest stage/tournament. Because VFL scoring only awards bonus points for rounds where a player earns 4 or more kills, "multi-kill rounds" for this stat are also considered rounds in which a player earns 4 or more kills.

**MK_MAP_CAREER** - "Multi-kill map recently" - averages a player's number of multi-kills per map over their career. Because VFL scoring only awards bonus points for rounds where a player earns 4 or more kills, "multi-kill rounds" for this stat are also considered rounds in which a player earns 4 or more kills.

### TEAM BASED FEATURES:

_(all team based features are collected over just the last stage/few tournaments to maintain relevancy)_

**MAP_WINS_AVG** - _"Map Wins Averaged"_ - averages the teams' total map wins in recent tournaments, helping us understand how many maps they tend to win across a whole tournament. This was chosen to account for the VFL scoring's 1 point awarded per map win per player. It stands to reason that players on teams that get further into tournaments and play more games will have more opportunities to get points in a more unique way than most other stats could account for. We chose to average total wins in a tournament run and not a win percentage to leverage the VFL scoring rules' lack of a penalty for losing maps and to emphasize longer tournament runs with more team-based scoring opportunities.

**BO3_SHUTOUT_PERC** - _"Best of three shutout percentage"_ - divides a team's number of 2-0 victories by the total number of best of 3 games the team has played. Accounts for VFL scoring's 2 bonus points for 2-0 victories.

**BO5_SHUTOUT_PERC** - _"Best of five shutout percentage"_ - divides a team's number of 3-0 victories by the total number of best of 5 games the team has played. Accounts for VFL scoring's 4 bonus points for 3-0 victories.

**BO5_3_TO_1_PERC** - _"Best of five three to one percentage"_ - divides a team's number of 3-1 victories by the total number of best of 5 games the team has played. Accounts for VFL scoring's 1 bonus point for 3-1 victories.

**SHUTOUT_PERC** - _"Shutout percentage"_ - divides a team's total number of 13-0 victories by their total maps played. Accounts for VFL scoring's 5 bonus points for a 13-0 map win.

**TEN_ROUNDS_PERC** - _"Ten rounds percentage"_ - divides a team's total number of victories that include a round gap of 10 or more by the total number of maps played. Accounts for VFL scoring's +2 bonus points for a win that includes at least a 10-round gap.

**FIVE_ROUNDS_PERC** - _"Five rounds percentage"_ - divides a team's total number of victories with a round win gap of 5-9 by the total number of maps played. Accounts for VFL scoring's 1 bonus points for a 5-9 round gap map win.

**OPP_SHUTOUT_PERC** - _"Opponent shutout percentage"_ - or, more accurately, "Shutout by opponent percentage" divides a team's total number of 0-13 losses by their total number of maps played. Accounts for VFL scoring's -5 point penalty for a 0-13 map loss.

**OPP_TEN_ROUND_PERC** - _"Opponent ten round percentage"_ - divides a team's total number of losses that includes a round gap of 10 or more by their total number of maps played. Accounts for VFL scoring's -1 point penalty for a loss that includes at least a 10-round gap.

