from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict, cross_val_score
import pandas as pd
import numpy as np

location = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(location)
print(df.info())

x = df[['highway-mpg', 'engine-size', 'normalized-losses', 'horsepower', 'peak-rpm']]
y = df['price']

lm = LinearRegression()
lm.fit(x, y)

yHat = cross_val_predict(lm, x, y, cv=3)
print(yHat)

scores = cross_val_score(lm, x, y, cv=3)
print('cross_val_scores:\n', scores)
print('mean_score: ', np.mean(scores))
