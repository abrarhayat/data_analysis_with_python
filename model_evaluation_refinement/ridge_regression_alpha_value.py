from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

df = pd.read_csv(
    'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv')
x = df[['highway-mpg', 'engine-size', 'normalized-losses', 'horsepower', 'peak-rpm']]
y = df['price']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

alpha_values = [0, 0.001, 0.01, 1, 10]
mse_list = []
rsq_list = []
for value in alpha_values:
    RidgeModel = Ridge(alpha=value)
    RidgeModel.fit(x_train, y_train)
    prediction = RidgeModel.predict(x_test)
    mse = mean_squared_error(y_test, prediction)
    rsq = r2_score(y_test, prediction)
    mse_list.append(mse)
    rsq_list.append(rsq)

print('alpha_values:', alpha_values)
print('mse_list:', mse_list)
print('rsq_list:', rsq_list)
