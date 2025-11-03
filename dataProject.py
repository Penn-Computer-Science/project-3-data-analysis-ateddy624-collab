
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

df=pd.read_csv('surveyData.csv')
#df=pd.read_csv('realData.csv')
mySurveyData=pd.DataFrame(df)

print(mySurveyData.info())
#print(mySurveyData)
dataPoints= 5
hours_exercising={"Time exercising" : "GPA"}

print("Average GPA by year:")
print(mySurveyData.groupby('hours_exercising')['GPA'].mean()) # Average GPA by year
print("-_"*40)
#This code was attempted but didn't work:
#for index, row in mySurveyData.iterrows():
    #hours_exercising[float(mySurveyData[row]['hours_exercising'])] = (mySurveyData[row]['GPA'])
#for i in range(dataPoints):
mySurveyData.groupby('hours_exercising')['GPA'].mean().plot(kind='bar', color='skyblue')
plt.title("Hours Exercising vs. GPA")
plt.xlabel("Hours Exercising")
plt.ylabel("GPA")
plt.tight_layout()
plt.show()


mySurveyData['hours_exercising'].plot(kind='hist', bins=4, color='purple', edgecolor='black')
plt.title("GPA Distribution")
plt.xlabel("GPA")
plt.ylabel("Number of Students")
plt.show()
print(hours_exercising)


plt.scatter(mySurveyData['hours_exercising'], mySurveyData['GPA'], alpha=0.6)
plt.title("GPA vs. hours exercising")
plt.xlabel("Hours exercising")
plt.ylabel("GPA")
plt.show()
#print(round(mySurveyData.describe()))
#GPAvsExercise=mySurveyData.groupby(hours_exercising)['GPA'].mean()
#print(GPAvsExercise)