import numpy as np 
import matplotlib.pyplot as plt 

X = np.linspace(0, 6, 50)
Y = 6 - X

w1 = np.array([[0, 0], [2,0], [2,2], [0,2]])
w2 = np.array([[4, 4], [6,4], [6,6], [4,6]])

def var(w):
    n = w.shape[0]
    m = w.mean(axis=0).T 
    C = np.cov(w.T) 
    C = C * (n-1) / n
    return m, C

def d_f(w1, w2, p1, p2):
    m1, C1 = var(w1)
    m2, C2 = var(w2)   

fig = plt.figure()
# 画图区域分成1行1列。选择第一块区域。
ax = fig.add_subplot(1,1, 1)
# 标题
ax.set_title("Discrimination Interface")
class1 = ax.scatter(w1[:,0], w1[:,1], color='r')
class2 = ax.scatter(w2[:,0], w2[:,1], color='b')

discriminator = ax.plot(X, Y, label='Distriminator')

ax.set_xlabel("x1")

ax.set_ylabel("x2")

plt.legend((class1, class2), ('Class w1', 'Class w2'), loc=0)

plt.show()