import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
scores = np.array([50, 55, 58, 60, 62, 65, 67, 70, 72, 75])

data = pd.DataFrame({'Hours': hours, 'Scores': scores})

#intercept
X = sm.add_constant(data['Hours'])
 

#model regression 
model = sm.OLS(data['Scores'], X).fit()


print(model.summary())


plt.scatter(data['Hours'], data['Scores'], label='Data Points')
plt.plot(data['Hours'], model.fittedvalues, color='red', label='Regression Line')
plt.xlabel('Hours of Study')
plt.ylabel('Scores')
plt.legend()
plt.title('Linear Regression: Hours vs Scores')
plt.show()


