from data_wrangling import dataframe_manager as dm
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

location = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = dm.get_clean_data_frame(location, headers)
print(df.head())

Z = df[['highway-mpg']]
Y = df['price']

lm = LinearRegression()

lm.fit(Z, Y)

coeff = lm.coef_
intercept = lm.intercept_
print('coeff: ',  coeff)
print('intercept: ', intercept)

# print(np.array(30).reshape(-1, 1))

# predict with a single value
predicted_result = lm.predict(np.array(30).reshape(-1, 1))
print('predicted_result: ', predicted_result)

# predict with multiple values
multiple_prices = np.arange(1, 101, 1).reshape(-1, 1)
predicted_result2 = lm.predict(multiple_prices)
print('predicted_result2: ', predicted_result2)

# Regplot pf the predicted values vs price
sns.regplot(predicted_result2, multiple_prices)

