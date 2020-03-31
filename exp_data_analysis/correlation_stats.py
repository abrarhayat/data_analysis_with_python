import pandas as pd
import data_wrangling.dataframe_manager as dm
import scipy.stats as scs

pd.set_option('display.max_columns', 200)
location = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
df = dm.create_df(location, headers)
print(dm.print_4_heads(df, ""))
dm.replace_cols_with_nan(df, ["price", "horsepower"])
dm.replace_cols_with_mean(df, ["price", "horsepower"])
df["price"] = df["price"].astype("float")
df["horsepower"] = df['horsepower'].astype('float')

#PEARSON Correlation
pearson_coeff, p_value = scs.pearsonr(df['horsepower'], df['price'])
print('pearson_coeff: ', pearson_coeff)
print('p_value: ', p_value)