import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



exam = pd.read_csv('C:\\Users\\user\\.spyder-py3\\Exam\\Exam.csv')

#SEE IF NaN VALUES EXISTS
print(exam.isna().any())

print(exam.info())
print(exam.head())
print(exam.dtypes)
print(exam.describe())

print(exam.select_dtypes('object').nunique())

print(exam.head())

math_s = list(exam["math score"])
read_s = list(exam["reading score"])


plt.scatter(math_s, read_s, s = 0.8)