# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# Importing the dataset
ipl_2008_2017 = pd.read_csv('ipl_2008_2017.csv')
X = ipl_2008_2017[["Match_No","player_id","inning","A_Avg_Runs","A_Avg_balls_Faced","avg_wick_a","A_Avg_Extras","O_Avg_Runs","O_Avg_balls_Faced","avg_wick_o","O_Avg_Extras"]]
runs = ipl_2008_2017.iloc[:, 17].values
wickets=ipl_2008_2017.iloc[:, 19].values


ipl_2018=pd.read_csv('ipl_2018.csv')
runs_bat_first = ipl_2018[["Match_No","player_id","inning","A_Avg_Runs","A_Avg_balls_Faced","avg_wick_a","A_Avg_Extras","O_Avg_Runs","O_Avg_balls_Faced","avg_wick_o","O_Avg_Extras"]]
runs_bat_second=ipl_2018[["Match_No","player_id","inning1","A_Avg_Runs","A_Avg_balls_Faced","avg_wick_a","A_Avg_Extras","O_Avg_Runs","O_Avg_balls_Faced","avg_wick_o","O_Avg_Extras"]]
wickets_first=ipl_2018[["Match_No","player_id","inning","A_Avg_Runs","A_Avg_balls_Faced","avg_wick_a","A_Avg_Extras","O_Avg_Runs","O_Avg_balls_Faced","avg_wick_o","O_Avg_Extras"]]
wickets_second=ipl_2018[["Match_No","player_id","inning1","A_Avg_Runs","A_Avg_balls_Faced","avg_wick_a","A_Avg_Extras","O_Avg_Runs","O_Avg_balls_Faced","avg_wick_o","O_Avg_Extras"]]
playing_xi=ipl_2018[["playing_xi_flag"]]

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X= sc.fit_transform(X)
runs_bat_first= sc.fit_transform(runs_bat_first)
runs_bat_second= sc.fit_transform(runs_bat_second)
wickets_first= sc.fit_transform(wickets_first)
wickets_second= sc.fit_transform(wickets_second)

model = Sequential()
model.add(Dense(13, input_dim=11, kernel_initializer='normal', activation='relu'))
#model.add(Dense(13, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal',activation='relu'))
# compile model

model.compile(loss='mean_squared_error', optimizer='adam')

#model.compile(loss='mean_squared_error', optimizer='adam')

# fit the model for runs
model.fit(X, runs, batch_size=5, epochs=50, verbose=0)

#ipl prediction
#runs
run_pred_first=model.predict(runs_bat_first)
run_pred_second=model.predict(runs_bat_second)

np.savetxt("run_pred_second.csv", run_pred_second, delimiter=",")
#fit the model for wickets
model.fit(X, wickets, batch_size=5, epochs=50, verbose=0)
#ipl prediction
#wickets
wicket_pred_first=model.predict(wickets_first)
wicket_pred_second=model.predict(wickets_second)



submission=pd.read_csv("player_predictions.csv")


submission["runs_scored_bat_first"] = run_pred_first
submission["runs_scored_bat_second"] = run_pred_second
submission["wickets_taken_bowl_first"] = wicket_pred_first
submission["wickets_taken_bowl_second"] = wicket_pred_second
submission["playing_xi_flag"] = playing_xi
submission.to_csv("player_predictions123.csv")
