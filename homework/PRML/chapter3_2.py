import numpy as np 

C = 1 
W = np.array([0,0,0,0]) # 初始化 W 为 [0,1,1] (3,1)
w1 = np.array([[0,0,0], [1,0,0], [1,0,1], [1,1,0]]) # (4,3)
w2 = np.array([[0,0,1], [0,1,1], [0,1,0], [1,1,1]])
b1 = np.ones((w1.shape[0],1)).astype(np.int32)
b2 = np.ones((w2.shape[0],1)).astype(np.int32)
w1 = np.c_[w1, b1]
w2 = np.c_[w2, b2]
w2 = -w2 
n1 = len(w1)
n2 = len(w2)

flag = True # 是否需要继续计算
m = 0
while(flag):
    print('iteration: ', m)
    m+=1
    flag = False # 首先设为flase，如果有错误，则继续迭代
    for i in range(n1):
        x1 = w1[i, :]
        y1 = (x1*W).sum()
        if(y1<=0):
            flag = True
            W += C*x1
    for i in range(n2):
        x2 = w2[i, :]
        y2 = (x2*W).sum()
        if(y2<=0):
            flag = True
            W += C*x2

print(W)

