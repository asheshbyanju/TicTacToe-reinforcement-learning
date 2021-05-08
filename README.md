# Battle Between Two Tic-Tac-Toe Reinforcement Agents
Tic tac toe is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner. <br />
In this project, I intended to develop a agent who will learn how to play tic tac toe and compete again other players. Main objective of the project is to train the agent to learn the strategy to find the best available move and beat Random Agent. I will be using reinforcement Q-Learning to achieve goal.

## Overview
* I use two strategies: (Random and Q-Learning) 
* Will play 4 games: Random vs Random, Random vs Q-learning, Q-learning vs Random and Q-Learning vs Q-Learning
* Will play 10,000 games using each strategy and after the games are played we will gather our statistics and plot the results to see how Q-Learning agent performed.

## Installation
### Requirements
Codes are writtern in python and requires python 3.6 + to run.

### Running code
Instructions on how to run the project:<br>
**Step 1:** Download the zip file or clone the repository <br>
**Step 2:** cd to the directory where your downloaded folder is located.<br>
**Step 3:** run: `pip install -r requirements.txt` in your shell <br>
**Step 4:** open the folder in spyder <br>
**Step 5:** open main.py and run

## Results
Q-Learning Player vs Q-Learning Player <br>
==================== <br>
Train result - 10000 games <br>
Q-Learning win: 2322 (23%) <br>
Q-Learning win: 691 (6%) <br>
Draw: 6986 (69%) <br> 
==================== <br><br>
Q-Learning Player vs Random Player <br>
==================== <br>
Train result - 10000 games <br>
Q-Learning win: 9197 (91%) <br>
Random win: 397 (3%) <br>
Draw: 405 (4%) <br>
==================== <br>

