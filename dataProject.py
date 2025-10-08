
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

df=pd.read_csv('C:Documents\GitHub\project-3-data-analysis-ateddy624-collab\surveyData.csv')
mySurveyData=pd.DataFrame(df)

#print(mySurveyData.info())
#print(mySurveyData)

print(round(mySurveyData.describe()))
GPAvsExercise=mySurveyData.groupby('hours_exercising')['GPA'].mean()
print(GPAvsExercise)