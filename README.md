# VFL Neural Network Model Studio

VFL Neural Network Studio is an interactive 100% client-side web application where users can create, train, visualize, and analyze custom neural networks entirely in the browser. Created models are used to predict the VALORANT Fantasy League (VFL) scores of professional VALORANT players. 

Built around a zero-dependency vanilla JavaScript engine developed specifically for this project called [benutils](https://github.com/BenPask/benutils), the engine features linear algebra/matrix math utilities, model architecture templates, model training via .csv or .json data, as well as PRNG (for weight initialization), and a custom canvas scatterplot graphing module. The training data was collected from an API for [vlr.gg](https://www.vlr.gg/), a popular stats/news resource in the VALORANT esports space.

Authors: Benjamin Pask, Clay Wright, Jackson Bowers, and Ian Collins. 

### This project was created as a proof of concept for a student-led development group. Following its success, the four of us have expanded our team, formalized our workflow, and are now taking on larger-scale projects.

<img width="2000" height="700" alt="vfl model credit" src="https://github.com/user-attachments/assets/741dda4a-5562-4aee-a8d3-13e83e86b958" />

# Model Info

On VFL Neural Network Model Studio, users create, train, and visualize a regression-based neural network prediction model to predict a list of professional VALORANT players' VFL points, a metric created by the VALORANT Fantasy League developers to reflect a holistic measure of player performance. We selected and created the features for potential models based on the VFL scoring rules found [here](https://www.valorantfantasyleague.net/rules) . For a full list of the features used and explanations of their meaning and relevance to the project, you may visit the ["Feature List"](#feature-list) section of this file.

All models created on the website are built using benutils, the API developed for this project. More extensive documentation regarding benutils and its functions is available [here](https://github.com/BenPask/benutils).

# Model Creation Options

### Hidden Layer Count - Specifies the number of hidden layers in the model.

### Initial Layer Size - Specifies the number of neurons in the first hidden layer. The following hidden layer sizes are determined by the selected architecture type.

### Architecture Type - The shape and hidden layer sizes of the model. Users pick from the following options:</br>
_(All examples were generated using shape-showcasing sizes that are not meant to reflect good model engineering practices for our dataset)_

**Flat**
_(Generated with a hidden layer count of 5 and an initial layer size of 5)_
<img width="600" height="372" alt="flat arch" src="https://github.com/user-attachments/assets/6872569d-85a1-47db-b4ab-bf35ce10cc56" /></br>

**Po2**
_(Generated with a hidden layer count of 6 and an initial layer size of 16)_ </br>
<img width="600" height="372" alt="po2 arch" src="https://github.com/user-attachments/assets/d4ed0f8e-4df9-4a66-89bc-b4985cf6083e" /></br>
_(Not visible: initial layer size automatically becomes the closest power of 2 to the number provided)_ </br>
_(Architecture functions automatically space out their operations to create clean, predictable shapes)_

**Hourglass**
_(Generated with a hidden layer count of 7 and an initial layer size of 7)_ </br>
<img width="600" height="372" alt="hourglass arch" src="https://github.com/user-attachments/assets/9ae8c315-5a3d-418b-b6e9-2e32ed9ce490" /></br>
_(Options for hourglass operators are *, /, **, sqroot. Chosen operator gets inverted at the halfway point)_ </br>
_(User provided operation is used to determine the next layer size, in this example: hourglass operator = /, inverse op = *)_

### Hourglass Operator - Exclusively for Hourglass architecture, determines the operation applied to each hidden layer size.

### Activation - The function applied to every value being sent from one hidden layer to the next. The function does not get applied when sending values from the input layer to the first hidden layer, or from the final hidden layer to the output layer. There are 4 activation functions available in VFL NN Studio:

**ReLU** - Returns the input when x > 0 and 0 otherwise. Useful for its exceptional computational efficiency, though it can cause a risk of the [dying ReLU problem]([url](https://machinelearning.wtf/terms/dying-relu/)). 

**Leaky ReLU** - Same as ReLU, but returns a very small value instead of 0. Still efficient, and avoids the potential pitfall of dying neurons.

**Tanh** - Returns a value between -1 and 1, using tanh(x). More computationally expensive than ReLU, but useful when having a mean activation closer to 0 benefits your training strategy.

**Sigmoid** - Returns a value between 0 and 1 using a simple formula. Less computationally expensive than Tanh, but still more expensive than ReLU. Gradient updates are smoother than Tanh, which can be beneficial or not depending on your training strategy.

### Train/Test Split - A number from 0-1 that represents the percentage of the total observations dedicated to the test set. The test set is a subset of your observations that no longer uses the target feature and therefore is not used to train. It is used to evaluate the effectiveness of the model's training using metrics like MSE, RMSE, MAE, and R2. 

### Learn Rate - A simple constant that training changes are multiplied by to minimize the aggressiveness of the calculated changes to your model's weights and biases.

### Epochs - The number of times your model runs through the set of observations.

### Output Activation - Optionally, you can specify an activation function for only the output layer. By default, there is no activation, but it could make a difference  depending on your training strategy.

# Visualizing your model

### Once your created model finishes its training, scroll down to the model visualizer to evaluate its performance.

<img width="2819" height="1482" alt="Visualizer guide" src="https://github.com/user-attachments/assets/4a275c65-99b1-4391-9b9a-9d7c5952daae" />

### Text elements with the 📈 icon are hoverable elements that create scatterplots for deeper evaluation.

<img width="500" height="234" alt="image" src="https://github.com/user-attachments/assets/e6198657-ab41-4158-828b-9833cbc8f550" /> <img width="500" height="250" alt="image" src="https://github.com/user-attachments/assets/b4c40f29-9134-412f-a257-a83e9eab539b" />



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

