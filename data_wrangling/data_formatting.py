import pandas as pd
import numpy as np
import data_wrangling.dataframe_manager as dm

pd.set_option('display.max_columns', 200)

location = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(location)
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
df = dm.create_df(location, headers)
print(dm.print_4_heads(df, ""))
print('\n')

#changing units of a column from city-mpg to city-L/100km
print('\nChanging column name: ')
df['city-mpg'] = 235 / df['city-mpg']
df.rename(columns={"city-mpg": "city-L/100km"}, inplace=True)
print(df.head(4))

#Removing or replacing rows where price is not available
print(df.dtypes)
print('\n Removing or replacing rows where price is not available')
df.dropna(subset=["price"], axis=0, inplace=True)
df['price'].replace('?', 0, inplace=True)
df['price'].replace(np.nan, 0, inplace=True)
print(df.head())

print('\nChanging dtype for price from object to float64: ')
df["price"] = df["price"].astype('float')
print(df.dtypes)
