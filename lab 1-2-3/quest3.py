import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

dt1 = pd.read_csv('lab 1-2-3/sample.1.csv')
dt2 = pd.read_csv('lab 1-2-3/sample.2.csv')
dt3 = pd.read_csv('lab 1-2-3/sample.3.csv')
dt4 = pd.read_csv('lab 1-2-3/sample.4.csv')
dt5 = pd.read_csv('lab 1-2-3/sample.5.csv')
dt6 = pd.read_csv('lab 1-2-3/sample.6.csv')
dt7 = pd.read_csv('lab 1-2-3/sample.7.csv')
dt8 = pd.read_csv('lab 1-2-3/sample.8.csv')
dt9 = pd.read_csv('lab 1-2-3/sample.9.csv')
dt10 = pd.read_csv('lab 1-2-3/sample.10.csv')

# a)
# First we calculate mean of 10 samples
x1 = dt1['View'].mean()
x2 = dt2['View'].mean()
x3 = dt3['View'].mean()
x4 = dt4['View'].mean()
x5 = dt5['View'].mean()
x6 = dt6['View'].mean()
x7 = dt7['View'].mean()
x8 = dt8['View'].mean()
x9 = dt9['View'].mean()
x10 = dt10['View'].mean()
# Then add it to a list and draw histogram
ls = {x1,x2,x3,x4,x5,x6,x7,x8,x9,x10}
q3 = pd.DataFrame(ls, columns= ['mean'])
plt.figure(figsize=(8,6))
plt.hist(q3['mean'], width = 0.79, bins= 'auto')
plt.title('Histogram of mean')
plt.show()

# b)
# Calculate range
q3b = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
rg = (min(q3b),max(q3b))
print(rg)
# Calculate standard deviation of 10 samples
x1b = dt1['View'].std()
x2b = dt2['View'].std()
x3b = dt3['View'].std()
x4b = dt4['View'].std()
x5b = dt5['View'].std()
x6b = dt6['View'].std()
x7b = dt7['View'].std()
x8b = dt8['View'].std()
x9b = dt9['View'].std()
x10b = dt10['View'].std()
# Calculate variance of 10 samples
x1c = dt1['View'].var()
x2c = dt2['View'].var()
x3c = dt3['View'].var()
x4c = dt4['View'].var()
x5c = dt5['View'].var()
x6c = dt6['View'].var()
x7c = dt7['View'].var()
x8c = dt8['View'].var()
x9c = dt9['View'].var()
x10c = dt10['View'].var()

