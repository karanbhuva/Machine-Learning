# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:09:02 2020

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data1=pd.read_csv("Salary_Data.csv")
data=data1.values.tolist()

x=[]
y=[]
for i in range(len(data)):
    x.append(data[i][0])
    y.append(data[i][1])

x=np.array(x).reshape((-1,1))
y=np.array(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=LinearRegression().fit(x_train, y_train)

a=model.coef_
b=model.intercept_


print("\nSlope is:",a)
print("\nIntercept is:",b)


g=[min(x_train),max(x_train)]
c=[]
for i in range(len(g)):
    c.append((model.coef_* g[i])+model.intercept_)
    
plt.plot(g,c,color="red")
plt.title("Linear Regression")
plt.scatter(x,y)
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

#Prediction
prediction=[]
for i in range(len(x_test)):
    prediction.append((model.coef_* x_test[i])+model.intercept_)