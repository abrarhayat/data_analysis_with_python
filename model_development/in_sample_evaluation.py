from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from data_wrangling import dataframe_manager as dm

location = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = dm.get_clean_data_frame(location, headers)
print(df.head())

Z = df[['highway-mpg', 'horsepower', 'curb-weight', 'engine-size']]
Y = df['price']

lm = LinearRegression()

# train the model
lm.fit(Z, df['price'])

# get the prediction
Yhat = lm.predict(Z)

# Mean Squared Error
mse = mean_squared_error(Y, Yhat)
print('mean_squared_error:', mse)

# R-squared / R^2
r_sq = lm.score(Z, Y)
print('R-Sqaured: ', r_sq)