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
dm.replace_cols_with_nan(df, ["price"])
dm.replace_cols_with_mean(df, ["price"])
df["price"] = df["price"].astype("float")



#GROUP BY
print('\n')
print("GROUP BY DEMO")
df_test = df[['drive-wheels', 'body-style', 'price']]
df_grp = df_test.groupby(['drive-wheels', 'body-style']).mean()
print(df_grp)

#PIVOT
print('\n')
print("PIVOT Table DEMO")
df_pivot = df_grp.pivot(index='drive-wheels', columns=['body-style'])
print(df_pivot)