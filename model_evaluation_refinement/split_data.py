from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns

location = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(location)

x = df[['highway-mpg', 'engine-size', 'normalized-losses', 'horsepower', 'peak-rpm']]
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

lm = LinearRegression()
lm.fit(x_train, y_train)

# Testing the model with test data
prediction = lm.predict(x_test)
print(prediction)

ax1 = sns.distplot(x, y, hist=False, color='r')
ax2 = sns.distplot(x_test, prediction, hist=False, color='b', ax=ax1)