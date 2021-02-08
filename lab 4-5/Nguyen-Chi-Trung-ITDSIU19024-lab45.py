import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sbs
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Import data from csv file and set their attribute
dt = pd.read_csv('AutoSurvey.csv',sep=',',header=0,usecols= [0,1,2,3,4,5], 
dtype={0:str, 1:str, 2:str, 3:np.float64, 4:np.int32, 5:np.float64})
dt.columns = ['Gender','Type', 'Purchased', 'VehicleAge', 'Mileage', 'MPG']
#Print data 
print(dt.iloc[1:21])

# Encoding categorical variable
gender_var = dt['Gender']
gender_var[gender_var == 'Male'] = 1
gender_var[gender_var == 'Female'] = 0

type_var = dt['Type']
type_var[type_var == 'Small'] = 1
type_var[type_var == 'Mid-size'] = 2
type_var[type_var == 'Minivan'] = 3
type_var[type_var == 'Small SUV'] = 4
type_var[type_var == 'Large SUV'] = 5

purchase_var = dt['Purchased']
purchase_var[purchase_var == 'Used'] =  1
purchase_var[purchase_var == 'New'] = 0

vehicleAge_var = dt['VehicleAge']

mileage_var = dt['Mileage']

mpg_var = dt['MPG']

variable = [gender_var, type_var, purchase_var, vehicleAge_var, mileage_var, mpg_var]

#Calculate descriptive statistic and display the chart
for var in variable:
    #Name of chart
    print(var.name)
    #Mean of column
    print(f'Mean = {np.mean(var):.2f}')
    #Variance of column
    print(f'Variance = {np.std(var):.2f}')
    #Standard deviation of column
    print(f'Standard deviation = {np.var(var):.2f}')
    #Show histogram and cumulative frequency line 
    sbs.distplot(var)
    plt.show()

# Calculate jointly distributed
joint_prob,ranges=np.histogramdd(variable)
joint_prob /= joint_prob.sum()
ranges=ranges[-1]

#Calculate the marginal probability distribution of MPG and estimate probability of MPG
marginal_prob=[]
for i in range(10):
    marginal_prob.append(np.sum(joint_prob[:, :, :, :, :, i]))

for (x, y_x) in enumerate(marginal_prob):
    print(f'P({ranges[x]:.2f}  < MPG <  {ranges[x + 1]:.2f}) = {y_x:.2f}')

#Build a linear regression to predict value
dt1 = dt.tail()
X = dt1.iloc[:, :-1].values
y = dt1.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 3, random_state = 0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predict and compare with the actual
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)