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
print(df.head(5))


#add 1 to all rows in column
df['symboling'] = df['symboling'] + 1
print('\n After adding 1')
print(df.head(2))

#counts of particular columns
print('\nInfo on counts')
print(df['num-of-doors'].value_counts())
print(df['num-of-doors'].value_counts().idxmax())

#Which values are missing?
print('\n')
print("Info on missing values: ")
missing_data = df.isnull()
print(missing_data.head(5))
print('\n')
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")
print('\n')


#REPLACING values in rows
#replace missing prices with meanPrice price
print('\n')
#First Replace ? with nan
df['price'].replace('?', np.nan, inplace=True)
meanPrice = df['price'].astype('float').mean(axis=0)

df['price'].replace(np.nan, meanPrice, inplace=True)
print(df.head(20))

#REMOVING rows
#we can drop missing values along the column "price" as follows
#axis 0, or ‘index’ : Drop rows which contain missing values.
#axis 1, or ‘columns’ : Drop columns which contain missing value.
print('\n Removing rows where price is not available')
df.dropna(subset=["price"], axis=0, inplace = True)
#if inplace was not used
#df = df.dropna(subset=["price"], axis=0)

#reseting index as we dropped rows
df.reset_index(drop=True, inplace=True)
print(df.head(20))


