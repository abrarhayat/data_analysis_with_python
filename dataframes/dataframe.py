import pandas as pd

pd.set_option('display.max_columns', 200)


# for printing all column names
def print_all_df_column_names(dataframe):
    column_names = ''
    for col in dataframe:
        print(col)
        column_names = column_names + "\'" + col + "\'" + ', '
    print('\n')
    print("column_names: ", column_names)


location = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
# df = pd.read_csv(location, header='none')
df = pd.read_csv(location, header=None)

#show only the first n rows before adding column names
print(df.head(5))
print('\n')

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# set headers
df.columns = headers

#show only the first n rows after adding column names
print(df.head(5))
print('\n')

#show the last n rows
print(df.tail(2))
print('\n')

# show types of data in each column
print(df.dtypes)
print('\n')

# show stats on df
print(df.describe())
print('\n')

# show stats on all columns even object type ones
print(df.describe(include='all'))
print('\n')


#we can drop missing values along the column "price" as follows
#axis 0, or ‘index’ : Drop rows which contain missing values.
#axis 1, or ‘columns’ : Drop columns which contain missing value.
df.dropna(subset=["price"], axis=0)
print('\n')

#save the data into a new csv
df.to_csv("dataframes/automobile.csv", index=False)
print('\n')

#new df by specifying column names
df[['length', 'compression-ratio']]

#describe the new df
df[['length', 'compression-ratio']].describe()
print('\n')

#concise summary of the df
print(df.info)

