
# IMPORTING THE LIBDRARIES

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# IMPORTING THE DATASET
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

# TRAINING THE DECISON TREE REGRESSION ON THE WHOLE DATA
from sklearn.ensemble import RandomForestRegressor
regressor =RandomForestRegressor(n_estimators=10,random_state = 0)
regressor.fit(X, y)

# Predicting a new result
regressor.predict([[6.5]])


# Visualising the Decision Tree Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()