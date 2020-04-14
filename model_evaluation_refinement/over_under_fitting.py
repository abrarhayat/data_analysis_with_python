from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

location = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(location)

x = df[['horsepower']]
y = df['price']

lr = LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

Rsqu_test = []

order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for n in order:
    pr = PolynomialFeatures(degree=n)
    # making polynomial inputs for x_train and x_test
    x_train_pr = pr.fit_transform(x_train)
    x_test_pr = pr.fit_transform(x_test)

    lr.fit(x_train_pr, y_train)
    # adding the scores of different orders to a list
    Rsqu_test.append('Order' + str(n) + ', r_sq: ' + str(lr.score(x_test_pr, y_test)))


print('Rsqu_test: ', Rsqu_test)