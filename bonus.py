import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('Electric_Vehicle_Population_Data.csv',nrows=500)
train_size=0.8
file_name = df[['Model Year','Postal Code','Make','Model','Electric Vehicle Type','Electric Range']]

x = file_name.drop(columns=['Electric Range'])
print(x)
y = df['Electric Range']
print(y)

x_train, x_rem, y_train, y_rem = train_test_split(x,y,train_size=0.8)


x_valid, x_test, y_valid, y_test = train_test_split(x_rem, y_rem,test_size=0.2)

print('Training Data Count: {}'.format(x_train.shape[0]))
print('Testing Data Count: {}'.format(x_test.shape[0]))

print(x_train.shape), print(y_train.shape)
print(x_valid.shape), print(y_valid.shape)
print(x_test.shape), print(y_test.shape)
