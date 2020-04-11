import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/home/abrar/data_analysis_with_python/data_wrangling/clean_df.csv")
#print(df.head())

Z = df[['city-L/100km', 'horsepower', 'curb-weight', 'engine-size']]
Y = df['price']

lm = LinearRegression()

#train the model
lm.fit(Z, df['price'])

#get the prediction
Yhat = lm.predict(Z)
print(Yhat)

print(len(Z))
print(len(Yhat))

#the parameters
b0 = lm.intercept_
b_others = lm.coef_
print(b0)
print(b_others)