from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
X,y = load_diabetes(return_X_y=True, as_frame=False)
print(type(X))
a =np.array([[1, 2], [3, 4],[5,6]])
b = np.array([5, 6, 7]).reshape(-1,1)
c = np.hstack((a,b))
np.random.shuffle(c)
colNum = c.shape[1]
x  = c[-2:,:]
print(X.shape[0])
print(X.shape[1])
print(y.shape[0])
data = np.concatenate((X, y), axis=0)
print("1")