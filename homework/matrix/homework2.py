import numpy as np 

def LUDecompose(A):
    N = A.shape[0]
    P, L = np.eye(N), np.zeros((N,N)) # P 初始化一个 I 矩阵，L矩阵初始化为一个0矩阵
    for i in range(N):
        j = np.argmax(A[i:, i]) + i  # 找到当前列的从i开始的最大值，然后进行交换
        A = interchange(A, i, j)
        P = interchange(P, i, j) # 同样的，需要对P和L 进行交换
        L = interchange(L, i, j)
        pivot = A[i,i] # 保存主元
        print('STEP ', i+1, '   ', pivot)
        for k in range(i,N):
            L[k,i] = A[k,i]/pivot
        for m in range(i+1,N):
            for n in range(i+1,N):
                A[m,i] = 0
                A[m,n] -= L[m,i] * A[i, n]
        print(A)
        print(L)

    return P, L, A  # 这里的A经过变化，已经处理为U 

def interchange(A, i, j):
    A[[i,j], :] =  A[[j,i], :]
    return A 

if __name__ == '__main__':
    A = np.array([[1,2,4,17], [3,6,-12,3], [2,3,-3,2],[0,2,-2,6]])
    print(A)

    P, L ,U = LUDecompose(A)
    print(P)
    print(L)
    print(U)
