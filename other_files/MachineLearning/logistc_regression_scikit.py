# imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def load_data(path, header):
    marks_df = pd.read_csv(path, header=header)
    return marks_df


if __name__ == "__main__":
    # load the data from the file
    data = load_data("C:/Users/vajravel/Desktop/Eethalview/other_files/MachineLearning/marks1.txt", None)

    # X = feature values, all the columns except the last column
    X = data.iloc[:, :-1]

    # y = target values, last column of the data frame
    y = data.iloc[:, -1]

    # filter out the applicants that got admitted
    admitted = data.loc[y == 1]

    # filter out the applicants that din't get admission
    not_admitted = data.loc[y == 0]

    # plots
    plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Admitted')
    plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10, label='Not Admitted')
    plt.legend()
    plt.show()

    #-----------------------------------------------------------
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score 
    model = LogisticRegression()

    # create a model using X, y values from the file
    model.fit(X, y)

    # Now, predict classes using the same X values
    predicted_classes = model.predict(X)
    print("Predicted_classes: ", predicted_classes)

    # find accuracy using predicted classes and y values
    #accuracy = accuracy_score(y.flatten(),predicted_classes)

    #predicted_classes
    #parameters = model.coef_
    #print("Parameters: ", parameters)