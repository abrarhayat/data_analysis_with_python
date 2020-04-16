from sklearn.linear_model import Ridge
import pandas as pd
import seaborn as sns

df = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv')

x = df[['highway-mpg', 'engine-size', 'normalized-losses', 'horsepower', 'peak-rpm']]
y = df['price']

RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(x, y)

yHat = RidgeModel.predict(x)

ax1 = sns.distplot(x, y, hist=False, color='r')
ax2 = sns.distplot(x, yHat, hist=False, color='b', ax=ax1)
