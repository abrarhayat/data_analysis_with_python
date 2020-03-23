import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 200)


location = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
# df = pd.read_csv(location, header='none')
df = pd.read_csv(location, header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers         
print(df.head(20))


#add 1 to all rows in column
df['symboling'] = df['symboling'] + 1
print('\n After adding 1')
print(df.head(2))


#we can drop missing values along the column "price" as follows
#axis 0, or ‘index’ : Drop rows which contain missing values.
#axis 1, or ‘columns’ : Drop columns which contain missing value.
print('\n Removing rows where price is not available')
df.dropna(subset=["price"], axis=0, inplace = True)
#if inplace was not used 
#df = df.dropna(subset=["price"], axis=0)
print(df.head(20))


#replace missing prices with meanPrice price
meanPrice = df['price'].mean()

df['price'].replace(np.nan, meanPrice)
print('\n Replace ? with mean')
print(df.head(20))


