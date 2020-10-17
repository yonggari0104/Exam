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






#GRAPH OF MATH, READING, WRITING SCORES
plt.subplot(1, 3, 1)
sns.distplot(exam['math score'])

plt.subplot(1, 3, 2)
sns.distplot(exam['reading score'])

plt.subplot(1, 3, 3)
sns.distplot(exam['writing score'])

plt.suptitle('Checking for Skewness', fontsize = 18)
plt.show()


#FEMALE STUDENTS WITH +90 IN ALL SUBJECTS
print(exam[(exam['gender'] == 'female') &
     (exam['math score'] > 90) & 
     (exam['writing score'] > 90) &
     (exam['reading score'] > 90)])



#GROUP BY GENDER
print(exam.groupby(['gender']).agg(['min','median','max']))