import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

meals = pd.read_csv(''/kaggle/input/av-genpact-hack-dec2018/meal_info.csv'')
pd.set_option('precision',2)

meals.head()
meals.tail()
meals.describe()

print(meal.head())