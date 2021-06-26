import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/vajravel/Desktop/Eethalview/other_files/model/dat/card4.csv")

print(df.head(5))

plt.scatter(df['Element Type'],df['Number of Direct Stress'])