import pandas as pd
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



#NORMALIZATION

# normalizing the price with Simple Feature Scaling
df['price'] = df['price'] / df['price'].max()
print(dm.print_4_heads(df, "normalizing the price with Simple Feature Scaling"))

# normalizing the peak-rpm with Min-Max Method
df['peak-rpm'] = (df['peak-rpm'] - df['peak-rpm'].min()) / (df['peak-rpm'].max() - df['peak-rpm'].min())
print(dm.print_4_heads(df, "normalizing the peak-rpm with Min Max Method"))

# normalizing the curb-weight with z-score method
df['curb-weight'] = (df['curb-weight'] - df['curb-weight'].mean()) / df['curb-weight'].std()
print(dm.print_4_heads(df, "normalizing the curb-weight with z-score method"))
