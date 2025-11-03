import pandas as pd
import random

years=["Junior", "Senior"]
sport=["Baseball/softball", "Baskeball", "Cross Country", "Football", "Golf", "Soccer", "Swim & Dive", "Tennis", "Track & field", "Volleyball", "Wrestling", "Lacrosse", "None"]

fNames=["Mark", "Jimmy", "Andy", "Ben", "Calvin", "Conner", "James", "John", "Joe", "Timmy", "Billy", "Eli", "Ben", "Steven", "Marge", "Lisa"]
lNames=["Smith", "Jones", "Johnson", "Williams", "Brown", "Davis", "Rodrigues", "Miller", "Wilson", "Moore"]

names=[]

for i in range(20):
    names.append(f"{random.choice(fNames)}  {random.choice(lNames)}")


data={
    "Year": [random.choice(years) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.5),2) for _ in names],
    "hours exercising":[round(random.uniform(0,10), 1) for _ in names],
    "sport":[random.choice(sport) for _ in names],
    "hours practicing":[round(random.uniform(0,5), 1) for _ in names]
}

surveyData=pd.DataFrame(data)

print(surveyData)

surveyData.to_csv("surveyData.csv", index=False)