# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:28:28 2020

@author: mhayt
"""

print('\n\n')
print(' ---------------- START ---------------- \n')

#-------------------------------- API-FOOTBALL --------------------------------

#!/usr/bin/python
from os.path import dirname, realpath, sep, pardir
import sys
sys.path.append(dirname(realpath(__file__)) + sep + pardir + sep)


from ml_functions.data_processing import scale_df
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import cross_val_score


plt.close('all')

#------------------------------- ML MODEL BUILD -------------------------------

#importing the data and creating the feature dataframe and target series

with open('../prem_clean_fixtures_and_dataframes/2019_prem_df_for_ml_5_v2.txt', 'rb') as myFile:
    df_ml_5 = pickle.load(myFile)

with open('../prem_clean_fixtures_and_dataframes/2019_prem_df_for_ml_10_v2.txt', 'rb') as myFile:
    df_ml_10 = pickle.load(myFile)


#scaling dataframe to make all features to have zero mean and unit vector.
df_ml_10 = scale_df(df_ml_10, list(range(14)), [14,15,16])
df_ml_5 = scale_df(df_ml_5, list(range(14)), [14,15,16])


x_10 = df_ml_10.drop(['Fixture ID', 'Team Result Indicator', 'Opponent Result Indicator'], axis=1)
y_10 = df_ml_10['Team Result Indicator']

x_5 = df_ml_5.drop(['Fixture ID', 'Team Result Indicator', 'Opponent Result Indicator'], axis=1)
y_5 = df_ml_5['Team Result Indicator']



print('\nMULTILAYER PERCEPTRON\n')
#---------------------------- MULTILAYER PERCEPTRON ---------------------------


#split into training data and test data
x_train, x_test, y_train, y_test = train_test_split(x_10, y_10, test_size=0.2)

#instantiate the MLP classifier, and fit to the data
clf = MLPClassifier(hidden_layer_sizes=(18, 12), activation='logistic', random_state=0, max_iter=2000)
clf.fit(x_train, y_train)

#printing the cross-validation accuracy score
cv_score_av = round(np.mean(cross_val_score(clf, x_10, y_10))*100,1)
print('Cross-Validation Accuracy Score ML10: ', cv_score_av, '%\n')



# ----- GRID SEARCH -----

#creating the list of tuples to test the length of hidden layers
hidden_layer_test = []
for i in range(6,20,2):
    a = list(range(6,30,4))
    b = [i] * len(a)    
    c = list(zip(a, b))
    hidden_layer_test.extend(c)    
    
param_grid_grad = [{'hidden_layer_sizes':hidden_layer_test}]

#mlp gridsearch 
grid_search_grad = GridSearchCV(clf, param_grid_grad, cv=5, scoring = 'accuracy', return_train_score = True)
grid_search_grad.fit(x_10, y_10)

#Output best Cross Validation score and parameters from grid search
print('\n', 'Gradient Best Params: ' , grid_search_grad.best_params_)
print('Gradient Best Score: ' , grid_search_grad.best_score_ , '\n')

print(grid_search_grad.cv_results_['mean_test_score'])


#plotting the data

#populating df with x, y, z data
matrix_plot_data = pd.DataFrame({})
matrix_plot_data['x'] = list(zip(*hidden_layer_test))[0]
matrix_plot_data['y'] = list(zip(*hidden_layer_test))[1]
matrix_plot_data['z'] = grid_search_grad.cv_results_['mean_test_score']

#transforming z list into matrix format
Z = matrix_plot_data.pivot_table(index='x', columns='y', values='z').T.values

#getting x and y axis
X_unique = np.sort(matrix_plot_data.x.unique())
Y_unique = np.sort(matrix_plot_data.y.unique())

#instantiating figure and plotting heatmap with seaborn
fig, ax = plt.subplots()
im = sns.heatmap(Z, annot=True,  linewidths=.5)

#labelling x and y and title
ax.set_xticklabels(X_unique)
ax.set_yticklabels(Y_unique)
ax.set(xlabel='Hidden Layer 1 Length',
        ylabel='Hidden Layer 2 Length');
fig.suptitle('Cross Val Accuracy', y=0.95, fontsize=16, fontweight='bold');

#saving figure
fig.savefig('figures/testing_hidden_layer_lengths.png')    


# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')
