# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:48:36 2020

@author: Fernando



=== Linear Regression Formula ===
### Formula
y = a + b * x

a = y axis line Intercept (y value where x = 0)
b = slope of the regression line

How to calculate B
Slope (b) of regression line formula
### Formula
b = r * sy / sx

r = pearson correlation coeficient
    How to calculate (R) Pearson correlation coeficient
    ### Formula
    R = SUM((x - _x) * (y - _y)) / SQRT(SUM(x - _x)**2 * SUM(y - _y)**2)
    
    _x = The Mean value of x
    _y = The Mean value of y
    
sy = standard deviation of y
    ### Formula
    sy = SQRT(SUM(y - _y)**2 / n - 1)
sx = standard deviation of x
    sx = SQRT(SUM(x - _x)**2 / n - 1)


How to calculate A
Y-Intercept (a) of Regression line
### Formula
a = _y - b *_x
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean
from math import sqrt

# Indedependent variable - number of chimpanzees in hunting party
x = np.array([1,2,3,4,5,6,7,8])
# Dependent Variable - percent of successful hunts
y = np.array([30,45,51,57,60,65,70,71])

x_mean = mean(x)
# x_mean = sum(x)/len(x)
y_mean = mean(y)
# y_mean = sum(y)/len(y)

# Create (x - _x) and Create (x - _x)**2
x_minus_mean_x = []
sqrd_x_minus_mean_x = []
for i in range (len(x)):
    x_minus_mean_x.append(x[i] - x_mean)
    sqrd_x_minus_mean_x.append((x[i] - x_mean)**2)

# Create (y - _y) and Create (y - _y)**2
y_minus_mean_y = []
sqrd_y_minus_mean_y = []
for i in range (len(y)):
    y_minus_mean_y.append(y[i] - y_mean)
    sqrd_y_minus_mean_y.append((y[i] - y_mean)**2)

# Create (x - _x) * (y - _y) and x * y
x_times_y_mean = []
x_times_y = []
for i in range (len(x)):
    x_times_y_mean.append(x_minus_mean_x[i] * y_minus_mean_y[i]) 
    x_times_y.append(x[i] * y[i])

# Create the sum for (x - _x)**2, (y - _y)**2
sum_sqrd_x_minus_mean_x , sum_sqrd_y_minus_mean_y, = sum(sqrd_x_minus_mean_x), sum(sqrd_y_minus_mean_y)
# Create the sum for (x - _x) * (y - _y) and (x * y)
sum_x_times_y_mean, sum_x_times_y = sum(x_times_y_mean), sum(x_times_y)

# Calculate Pearson correlation coeficient
r = sum_x_times_y_mean / sqrt(sum_sqrd_x_minus_mean_x * sum_sqrd_y_minus_mean_y)

# Calculate y and x standard deviation
sy = sqrt(sum_sqrd_y_minus_mean_y / len(y) - 1)

sx = sqrt(sum_sqrd_x_minus_mean_x / len(x) - 1)

# Calculate B - Slope of regression line formula
b = r * (sy / sx)

# Calculate A - Y-Intercept (a) of Regression line
a = y_mean - b * x_mean

# Calculate Linear Regression Function for all X values
regression = a + b * x


# Plot the visualization
df = pd.DataFrame({'Number of Chimpanzees':x,'Percent Successful Hunts':y})
sns.scatterplot(x='Number of Chimpanzees',y='Percent Successful Hunts',data=df)
plt.plot(x, regression,'-g',label='chimp')