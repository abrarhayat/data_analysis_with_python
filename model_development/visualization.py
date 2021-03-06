import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from data_wrangling import dataframe_manager as dm

location = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = dm.get_clean_data_frame(location, headers)
print(df.head())

X = df[['highway-mpg']]
Y = df['price'].astype('float')

# create a linear regression object
lm = LinearRegression()

# fitting the modelling
params = lm.fit(X, Y)

# print(params)

# getting predictions
Yhat = lm.predict(X)

# plotting regression plots
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0, )

# plot residuals
sns.residplot(X, Y)

# distribution plots

ax1 = sns.distplot(Y, hist=False, color='r', label="Actual Value")
ax2 = sns.distplot(Yhat, hist=False, color='b', label="Fitted Values", ax=ax1)
