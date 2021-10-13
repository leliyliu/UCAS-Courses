import numpy as np 

# A = np.array([[1, 3, 1, -4], [-1, -3, 1, 0], [2, 6, 2, -8]])
# A = np.array([[1,1,1,1,1,1,1,1,1,1,1],[-5,-4,-3,-2,-1,0,1,2,3,4,5], [25,16,9,4,1,0,1,4,9,16,25]])
A = np.array([[1,1,1,1,1,1,1,1,1,1,1],[-5,-4,-3,-2,-1,0,1,2,3,4,5]])
b = np.array([2,7,9,12,13,14,14,13,10,8,4])

print(np.dot(A, A.T))
m = np.linalg.inv(np.dot(A, A.T))
print(m)
n = np.dot(A, b)
print(n)
x = (np.dot(m,n))

et = (np.dot(A.T, x) - b) 
error = np.dot(et.T, et)
print('error is {}'.format(error))