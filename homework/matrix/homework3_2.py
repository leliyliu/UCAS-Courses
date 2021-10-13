import numpy as np 

A = np.array([[1,2,-1],[0,-1,0],[1,0,7]])

Q = np.array([[1,1,1],[0,1,1],[0,0,1]])
Qt = np.linalg.inv(Q)

print(np.dot(np.dot(Qt, A), Q))