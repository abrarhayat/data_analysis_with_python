import pandas as pd
import numpy as np
import data_wrangling.dataframe_manager as dm

pd.set_option('display.max_columns', 200)

location = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
df = dm.create_df(location, headers)
print(dm.print_4_heads(df, ""))

# replacing price and peak-rpm missing values
print('\n Replacing rows where values are not available')
df = dm.replace_cols_with_nan(df, ['price', 'peak-rpm'])
df = dm.replace_cols_with_mean(df, ['price', 'peak-rpm'])

print('\nChanging dtype for price and peak-rpm from object to float64: ')
df[["price", "peak-rpm"]] = df[["price", "peak-rpm"]].astype('float')
#df[["price", "peak-rpm"]] = dm.change_col_types(df, ["price", "peak-rpm"], 'float')


#BINNING
#creating 3 bins for price
print('\nCreating Bins for price')
bins = np.linspace(df['price'].min(), df['price'].max(), 4)
#print(bins)
group_names = ["low", "medium", "high"]
#adding a new column to the df for binned price
df['binned-price'] = pd.cut(df['price'], bins, labels=group_names, include_lowest=True)
print(df.head(10))

