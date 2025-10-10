
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

df=pd.read_csv('C:Documents\GitHub\project-3-data-analysis-ateddy624-collab\surveyData.csv')
mySurveyData=pd.DataFrame(df)

print(mySurveyData.info())
#print(mySurveyData)
iterator=1
hours_exercising={"Time exercising" : "GPA"}
for index, row in mySurveyData.iterrows():
    iterator+=1
    hours_exercising[float(mySurveyData[row]['hours_exercising'])] = (mySurveyData[row]['GPA'])
print(hours_exercising)
#print(round(mySurveyData.describe()))
#GPAvsExercise=mySurveyData.groupby(hours_exercising)['GPA'].mean()
#print(GPAvsExercise)