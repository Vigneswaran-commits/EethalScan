import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score

df_train = pd.read_csv("C:/Users/vajravel/Desktop/Eethalview/other_files/MachineLearning/train.csv")
df_test = pd.read_csv("C:/Users/vajravel/Desktop/Eethalview/other_files/MachineLearning/test.csv")

# get independent x and dependent y data from train and test
x_train = df_train['x']
y_train = df_train['y']
x_test = df_test['x']
y_test = df_test['y']

# convert to array
x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

# put all values within a bracket
x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)

clf = LinearRegression(normalize=True)

# find the fit line using x train and y train data
clf.fit(x_train,y_train)

# using fit line, predict y values for x test data
y_pred = clf.predict(x_test)

# see how the predicted y values are close to real y values
print(r2_score(y_test,y_pred))