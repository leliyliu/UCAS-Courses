import numpy as np 

A = np.array([[4,-3,4],[2,-14,-3],[-2,14,0],[1,-7,15]])
R = np.array([[4,2,-2,1], [2,1,4,-2],[-2,4,1,2],[1,-2,2,4]])

print(np.dot(R,A))

q,r = np.linalg.qr(A)
print(q,r,np.dot(q,r))