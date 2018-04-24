## Import libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier ## GBM algorithm
from sklearn import cross_validation,metrics
#from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import GridSearchCV

import matplotlib.pylab as plt
#%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4

train = pd.read_csv('train_modified.csv')
target = 'Disbursed'
IDcol ='ID'

train['Disbursed'] = train.Disbursed.astype(int)

def modelfit(alg,dtrain, dtest, predictors, performCV=True, printFeatureImportance=True, cv_folds=5):
    alg.fit(dtrain[predictors], dtrain[target])
    dtrain_prediction = alg.predict(predictors)
    dtrain.predict_proba = (dtrain[predictors])[:, 1]