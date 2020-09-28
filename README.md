
<a href="http://matthaythornthwaite.pythonanywhere.com/"><img src="https://raw.githubusercontent.com/mhaythornthwaite/Football_Prediction_Project/master/web_server/static/images/Smart_Football_Predictor_Github_Logo_v2.png" alt="Smart Football Predictor" alt="Smart Football Predictor"></a>

<h4 align="center">View the Predictions Displayed in Simple Web Application <a href="http://matthaythornthwaite.pythonanywhere.com/" target="_blank">here</a>.
</h4>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)


## Table of Contents

<!--ts-->
* [Aims and Objectives](#Aims-and-Objectives)
* [Dataset](#Dataset)
* [Data Cleaning and Preparation](#Data-Cleaning-and-Preparation)
* [Feature Engineering and Data Visualisation](#Feature-Engineering-and-Data-Visualisation)
* [Model Selection and Training](#Model-Selection-and-Training)
* [Evaluation](#Evaluation)
* [Improvements](#Improvements)
<!--te-->


## Aims and Objectives

Through collection of past football data, a model was to be built that satisfied the following two objectives, one quantitative and one qualitative:

- Achieve a test accuracy of greater than 50%, with a stretch target of 60%.
- Output probabilities that appear sensible/realistic, that are comparable to odds offered on popular betting websites.


## Dataset

The data was collected directly from an API:<a href="https://www.api-football.com/" target="_blank"> api-football</a>. This was preferred over a static database that can be readily found online, due to the following:

- API calls can be made daily, refreshing the database with the most recent statistics and results, to consistently retrain the model on up-to-date information.
- The API not only provides past game data but information on upcoming games, essential to make predictions which feed into the web application.


## Data Cleaning and Preparation

Data was initially collected from the 2019-2020 premier league season, in the form of a single json file per fixture containing a range of stats (e.g. number of shots, possession etc.) These json files were loaded into a Pandas DataFrame, and organised into a nested dictionary in the following form: `{team ID: {fixture_id: stats_df}}` 

Execution of `01_api_data_request.py` and `02_cleaning_stats_data.py` will update the database with recently played fixtures and add these DataFrames directly to the nested dictionary described above. 

## Feature Engineering and Data Visualisation

In order to utilise as much previous match data as possible, whilst minimising the number of features, match data was averaged over the previous 10 games to predict an upcoming fixture. To understand how well a single team is performing, their average stats were subtracted from their opponent’s average stats, to produce a difference metric e.g. number of shots difference. A team with `number_of_shots_diff = 2` has taken on average 2 more shots than their opponent in the previous 10 games. Seven 'difference' features were chosen:

- Goal Difference
- Shot Difference
- Shots Inside The Box Difference
- Posession Difference
- Pass Accuracy Difference
- Corners Difference
- Fouls Difference

The above describes the features for a single team, hence the number of features is doubled to 14 when predicting a match. Like-for-like features were visualised in the following cross-plot, and demonstate that the chosen features have some influence on the outcome of a match.

<img src="https://raw.githubusercontent.com/mhaythornthwaite/Football_Prediction_Project/master/figures/average_10_games_team_target_result.png" alt="Figure 1">

<em>Figure 1. Green dots indicate a 'team' win and blue dots indicate an opponent win. Dots in the bottom left quadrant indicate a poor quality team and opponent, top left: low quality team and high quality opponent, top right: high quality team and opponent, bottom right: high quality team and low quality opponent.</em>


## Model Selection and Training

## Evaluation

## Improvements



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 
