from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("/home/abrar/data_analysis_with_python/data_wrangling/clean_df.csv")
#print(df.head())
X = df[['city-L/100km']]
Y = df[['price']]

#create a linear regression object
lm = LinearRegression()

#fitting the modelling
params = lm.fit(X,Y)

#print(params)

#getting predictions
Yhat = lm.predict(X)

print(type(Yhat))
print(Yhat)

#getting the attributes
b0 = lm.intercept_
b1 = lm.coef_
print("bo: ", b0)
print("b1: ", b1)
