import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file = pd.read_csv("Electric_Vehicle_Population_Data.csv", nrows = 500,)

file.dropna()
file.drop_duplicates()
file_name = file[['Model Year', 'Postal Code', 'Make', 'Model', 'Electric Vehicle Type', 'Electric Range']]
print(file_name)

print("\nElectric Range:")
print('Average: ',file_name['Electric Range'].mean())
print('Median: ',file_name['Electric Range'].median())
print('Standard Deviation: ',file_name['Electric Range'].std())

print("\nModel Year:")
print('Average:', file_name['Model Year'].mean())
print('Median:', file_name['Model Year'].median())
print('Standard Deviation:', file_name['Model Year'].std())

print("\nMode Postal Code:")
print(file_name['Postal Code'].mode().to_string())

x = np.array([file_name['Model Year']])
y = np.array([file_name['Electric Range']])

font1 = {'family': 'serif', 'color': 'blue', 'size' :20}
font2 = {'family': 'serif', 'color': 'red', 'size' :15}
plt.title('Electric Car range vs Year', fontdict=font1)
plt.xlabel('Model Year', fontdict=font2)
plt.ylabel('Electric Range', fontdict=font2)
plt.scatter(x, y)
plt.show()

ModelYear = file_name['Model Year'].value_counts().rename_axis('Year').reset_index(name= 'counts')
modelYear = ModelYear.sort_values(by = 'Year', ascending=True)
print('\n', modelYear)
plt.title('Model Year vs Number of Cars', fontdict=font1)
plt.xlabel('Model Year', fontdict=font2)
plt.ylabel('Number of Cars', fontdict=font2)
x1 = np.array([modelYear['Year']]).flatten()
y1 = np.array([modelYear['counts']]).flatten()
plt.bar(x1, y1)
plt.show()

MakeCount = file_name['Make'].value_counts().rename_axis('Make').reset_index(name= 'counts')
makeCount = MakeCount.sort_values(by='Make', ascending=False)
print('\n', makeCount)
plt.title('Make vs Number of Cars', fontdict=font1)
plt.xlabel('Number of Cars', fontdict=font2)
plt.ylabel('Make', fontdict=font2)
x2 = np.array([makeCount['counts']]).flatten()
y2 = np.array([makeCount['Make']]).flatten()
plt.barh(y2, x2)
plt.show()

TypeCount = file_name['Electric Vehicle Type'].value_counts().rename_axis('Type').reset_index(name = 'counts')
print('\n', TypeCount)
plt.title('Electric Vehicle Types', fontdict=font1)
arr = np.array([TypeCount['counts']]).flatten()
lable = TypeCount['Type'].to_list()
plt.pie(arr, labels=lable)
plt.show()
