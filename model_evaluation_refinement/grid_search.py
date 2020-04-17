from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
import pandas as pd

df = pd.read_csv(
    'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv')
x = df[['highway-mpg', 'engine-size', 'normalized-losses', 'horsepower', 'peak-rpm']]
y = df['price']

parameters = {'alpha': [0, 0.001, 0.01, 1, 10], 'normalize': [True, False]}
rr = Ridge()

# initializing the grid search with the model, parameters and no. of folds as input
grid_search = GridSearchCV(rr, parameters, cv=4, return_train_score=True)

grid_search.fit(x, y)

# print the best estimator config for the model
print('Best Estimator: ', grid_search.best_estimator_, '\n')

# print the results
scores = grid_search.cv_results_
# print(scores)
# print(scores.keys())

for param, mean_test_score, mean_train_score in zip(scores['params'], scores['mean_test_score'],
                                                    scores['mean_train_score']):
    print(param, "R^2 on test data:", mean_test_score, "R^2 on train data:", mean_train_score)
