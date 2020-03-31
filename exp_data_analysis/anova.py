import pandas as pd
import data_wrangling.dataframe_manager as dm
import scipy.stats as stats

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

#ANOVA - Analysis of Variance
#extracting relevant data
df_anova = df[["make", "price"]]
grouped_data = df_anova.groupby(["make"])
print("\ngrouped_data:" , grouped_data.head())

anova_results_1 = stats.f_oneway(grouped_data.get_group("honda")["price"], grouped_data.get_group("subaru")["price"])
print("anova_results_1:\n", anova_results_1)

anova_results_2 = stats.f_oneway(grouped_data.get_group("honda")["price"], grouped_data.get_group("jaguar")["price"])
print("anova_results_2:\n", anova_results_2)