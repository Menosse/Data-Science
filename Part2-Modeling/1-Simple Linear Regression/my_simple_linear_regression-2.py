# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:48:36 2020

@author: Fernando

=== Linear Regression Formula ===
Using Least Squares Line

* Needs x, y, x times y, x squared, y squared and sums
    m = slope
    b = y-intercept
    n = number of observations
    x = Independent variable
    y = dependent variable
    y_pred = regression line

### Formulas
    m = (n * (Σxy) - (Σx) * (Σy)) / (n * (Σxy ** 2) - (Σx ** 2))
    
    b = (Σy - m * (Σx)) / n
    
    y_pred = m * x + b
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''Create the variables and calculate the params to use on the equations'''
# Indedependent variable - number of chimpanzees in hunting party
x = np.array([1,2,3,4,5,6,7,8])
sum_x = sum(x)
x_sqrd = x**2
sum_x_sqrd = sum(x_sqrd)

# Dependent Variable - percent of successful hunts
y = np.array([30,45,51,57,60,65,70,71])
sum_y = sum(y)
y_sqrd = y ** 2
sum_y_sqrd = sum(y_sqrd)

# Independent Variable time Dependent Variable
x_time_y = []
for i in range(len(x)): x_time_y.append(x[i] * y[i])
sum_x_times_y = sum(x_time_y)

'''Calculate Linear Regression Function'''

# slope
m = (len(x) * sum_x_times_y - sum_x * sum_y) / (len(x)*sum_x_sqrd - sum_x**2)
#y-intercept
b = (sum_y - m * sum_x) / 8
# Regression
y_pred = m * x + b

# Plot the visualization
df = pd.DataFrame({'Number of Chimpanzees':x,'Percent Successful Hunts':y})
sns.scatterplot(x='Number of Chimpanzees',y='Percent Successful Hunts',data=df)
plt.plot(x, y_pred,'-g', label='chimp')