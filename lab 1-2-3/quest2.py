import pandas as pd 
# Import 10 samples
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

# Q2

# a)
# Item satisfied requirement should greater than mean so I used ...mean() to calculate mean
item1 = dt1[dt1['View'] > dt1['View'].mean()]
itemcount1 = sum(1 for row in item1['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 1 =', round((itemcount1/2000)*100,2),'%')
item2 = dt2[dt2['View'] > dt2['View'].mean()]
itemcount2 = sum(1 for row in item2['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 2 =',round((itemcount2/2000)*100,2),'%')
item3 = dt3[dt3['View'] > dt3['View'].mean()]
itemcount3 = sum(1 for row in item3['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 3 =',round((itemcount3/2000)*100,2),'%')
item4 = dt4[dt4['View'] > dt4['View'].mean()]
itemcount4 = sum(1 for row in item4['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 4 =',round((itemcount4/2000)*100,2),'%')
item5 = dt5[dt5['View'] > dt5['View'].mean()]
itemcount5 = sum(1 for row in item5['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 5 =',round((itemcount5/2000)*100,2),'%')
item6 = dt6[dt6['View'] > dt6['View'].mean()]
itemcount6 = sum(1 for row in item6['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 6 =',round((itemcount6/2000)*100,2),'%')
item7 = dt7[dt7['View'] > dt7['View'].mean()]
itemcount7 = sum(1 for row in item7['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 7 =',round((itemcount7/2000)*100,2),'%')
item8 = dt8[dt8['View'] > dt8['View'].mean()]
itemcount8 = sum(1 for row in item8['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 8 =',round((itemcount8/2000)*100,2),'%')
item9 = dt9[dt9['View'] > dt9['View'].mean()]
itemcount9 = sum(1 for row in item9['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 9 =',round((itemcount9/2000)*100,2),'%')
item10 = dt10[dt10['View'] > dt10['View'].mean()]
itemcount10 = sum(1 for row in item10['ItemId'])
print('Proportion of the items had more than the mean number of views of sample 10 =',round((itemcount10/2000)*100,2),'%')

# b)
# ...std() to calculate standard deviation of sample
item1b = dt1[dt1['View'] > (dt1['View'].mean() + dt1['View'].std())]
itemcount1b = sum(1 for row in item1b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 1 =',round((itemcount1b/2000)*100,2),'%')
item2b = dt2[dt2['View'] > (dt2['View'].mean() + dt2['View'].std())]
itemcount2b = sum(1 for row in item2b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 2 =',round((itemcount2b/2000)*100,2),'%')
item3b = dt3[dt3['View'] > (dt3['View'].mean() + dt3['View'].std())]
itemcount3b = sum(1 for row in item3b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 3 =',round((itemcount3b/2000)*100,2),'%')
item4b = dt4[dt4['View'] > (dt4['View'].mean() + dt4['View'].std())]
itemcount4b = sum(1 for row in item4b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 4 =',round((itemcount4b/2000)*100,2),'%')
item5b = dt5[dt5['View'] > (dt5['View'].mean() + dt5['View'].std())]
itemcount5b = sum(1 for row in item5b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 5 =',round((itemcount5b/2000)*100,2),'%')
item6b = dt6[dt6['View'] > (dt6['View'].mean() + dt6['View'].std())]
itemcount6b = sum(1 for row in item6b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 6 =',round((itemcount6b/2000)*100,2),'%')
item7b = dt7[dt7['View'] > (dt7['View'].mean() + dt7['View'].std())]
itemcount7b = sum(1 for row in item7b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 7 =',round((itemcount7b/2000)*100,2),'%')
item8b = dt8[dt8['View'] > (dt8['View'].mean() + dt8['View'].std())]
itemcount8b = sum(1 for row in item8b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 8 =',round((itemcount8b/2000)*100,2),'%')
item9b = dt9[dt9['View'] > (dt9['View'].mean() + dt9['View'].std())]
itemcount9b = sum(1 for row in item9b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 9 =',round((itemcount9b/2000)*100,2),'%')
item10b = dt10[dt10['View'] > (dt10['View'].mean() + dt10['View'].std())]
itemcount10b = sum(1 for row in item10b['ItemId'])
print('Proportion of the items that the number of views more than one standard deviation greater than the mean of sample 10 =',round((itemcount10b/2000)*100,2),'%')

# c)
item1c = dt1[(dt1['View'] >= (dt1['View'].mean() - dt1['View'].std())) & (dt1['View'] < (dt1['View'].mean() + dt1['View'].std()))]
itemcount1c = sum(1 for row in item1c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 1 =',round((itemcount1c/2000)*100,2),'%')
item2c = dt2[(dt2['View'] >= (dt2['View'].mean() - dt2['View'].std())) & (dt2['View'] < (dt2['View'].mean() + dt2['View'].std()))]
itemcount2c = sum(1 for row in item2c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 2 =',round((itemcount2c/2000)*100,2),'%')
item3c = dt3[(dt3['View'] >= (dt3['View'].mean() - dt3['View'].std())) & (dt3['View'] < (dt3['View'].mean() + dt3['View'].std()))]
itemcount3c = sum(1 for row in item3c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 3 =',round((itemcount3c/2000)*100,2),'%')
item4c = dt4[(dt4['View'] >= (dt4['View'].mean() - dt4['View'].std())) & (dt4['View'] < (dt4['View'].mean() + dt4['View'].std()))]
itemcount4c = sum(1 for row in item4c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 4 =',round((itemcount4c/2000)*100,2),'%')
item5c = dt5[(dt5['View'] >= (dt5['View'].mean() - dt5['View'].std())) & (dt5['View'] < (dt5['View'].mean() + dt5['View'].std()))]
itemcount5c = sum(1 for row in item5c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 5 =',round((itemcount5c/2000)*100,2),'%')
item6c = dt6[(dt6['View'] >= (dt6['View'].mean() - dt6['View'].std())) & (dt6['View'] < (dt6['View'].mean() + dt6['View'].std()))]
itemcount6c = sum(1 for row in item6c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 6 =',round((itemcount6c/2000)*100,2),'%')
item7c = dt7[(dt7['View'] >= (dt7['View'].mean() - dt7['View'].std())) & (dt7['View'] < (dt7['View'].mean() + dt7['View'].std()))]
itemcount7c = sum(1 for row in item7c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 7 =',round((itemcount7c/2000)*100,2),'%')
item8c = dt8[(dt8['View'] >= (dt8['View'].mean() - dt8['View'].std())) & (dt8['View'] < (dt8['View'].mean() + dt8['View'].std()))]
itemcount8c = sum(1 for row in item8c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 8 =',round((itemcount8c/2000)*100,2),'%')
item9c = dt9[(dt9['View'] >= (dt9['View'].mean() - dt9['View'].std())) & (dt9['View'] < (dt9['View'].mean() + dt9['View'].std()))]
itemcount9c = sum(1 for row in item9c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 9 =',round((itemcount9c/2000)*100,2),'%')
item10c = dt10[(dt10['View'] >= (dt10['View'].mean() - dt10['View'].std())) & (dt10['View'] < (dt10['View'].mean() + dt10['View'].std()))]
itemcount10c = sum(1 for row in item10c['ItemId'])
print('Proportion of the items that the number of views within one standard deviation of the mean of sample 10 =',round((itemcount10c/2000)*100,2),'%')