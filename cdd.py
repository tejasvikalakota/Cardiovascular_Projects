#Author:Tejasvi Kalakota
#

import warnings
warnings.filterwarnings('ignore')

import pandas as pd


#I use the pandas library to read excel file
df = pd.read_excel('CDD.xlsx', usecols=range(14), nrows=70000)


#Logisitic Regression

#scatter plot for CD vs BMI(visual)
import matplotlib.pyplot as plt
show_plot = input("Prescence of CD vs BMI(kgs)(yes/no): ")
if show_plot == "yes":
    import matplotlib.pyplot as plt
    plt.scatter(df.BMI, df.cardio, marker='+', color='red')
    plt.show()
else:
    print("Plot not shown")

#Train and fit model
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['BMI']], df['cardio'], test_size=0.1)
X_test
X_train
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)

#Display of Model Score
model_score = input("Calculate model score? (yes/no): ")
if model_score == "yes":
    score = model.score(X_test, y_test)
    print("Model score:", score)   
else:
    print("Model score not calculated.")


#note that lists are a data structure


#Predict probability of cardio disease for user input BMI
bmi = float(input("Enter BMI: "))

bmi_array = [[bmi]]
prediction = model.predict_proba(bmi_array)
print("Cardiovascular Disease Probability x(absence), y(prescence): ", prediction)

'''model.predict(X_test)
model.score(X_test,y_test)
model.predict_proba(X_test)'''



#Produces list and then Output file with BMI values 1-50 and predictions about the liklehood of CD
predictions = []

for bmi in range(1, 51):
    bmi_array = [[bmi]]
    prediction = model.predict_proba(bmi_array)
    predictions.append([bmi, prediction])
    
# Write predictions to file
with open('predictions.txt', 'w') as file:
    for p in predictions:
        file.write("BMI: {}, Prediction: {}\n".format(p[0], p[1]))

from custom_lib import Statistic, Mean, Median, Mode

# Calculate mean, median, and mode using custom lib for Age and BP 
#this is where I incorporate custom libary and OOP
basic_stats_age = input("Would you like to basic stats about the patients' ages in the Data set? (yes/no): ")
row_age = df.age.values.tolist()
mean = Mean(row_age).calculate()
median = Median(row_age).calculate()
mode = Mode(row_age).calculate()
if basic_stats_age =="yes":
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
else:
    print("Age Stats not calculated.")

basic_stats_blood = input("Would you like to basic stats about the patients' Diastolic blood pressure in the Data set? (yes/no): ")
row_blood = df.ap_lo.values.tolist()
mean2 = Mean(row_blood).calculate()
median2 = Median(row_blood).calculate()
mode2 = Mode(row_blood).calculate()
if basic_stats_blood =="yes":
    print("Mean:", mean2)
    print("Median:", median2)
    print("Mode:", mode2)
else:
    print("Diastolic blood pressure Stats not calculated.")
