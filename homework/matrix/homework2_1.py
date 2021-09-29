import numpy as np 

def PLUDecompose(A):
    N = A.shape[0]
    P, L = np.eye(N), np.zeros((N,N)) # P 初始化一个 I 矩阵，L矩阵初始化为一个0矩阵
    for i in range(N):
        j = np.argmax(abs(A[i:, i])) + i  # 找到当前列的从i开始的最大值，然后进行交换
        A = interchange(A, i, j)
        P = interchange(P, i, j) # 同样的，需要对P和L 进行交换
        L = interchange(L, i, j)
        pivot = A[i,i] # 保存主元
        for k in range(i,N):
            L[k,i] = A[k,i]/pivot
        for m in range(i+1,N):
            for n in range(i+1,N):
                A[m,i] = 0
                A[m,n] -= L[m,i] * A[i, n]

    return P, L, A  # 这里的A经过变化，已经处理为U 

def interchange(A, i, j):
    A[[i,j], :] =  A[[j,i], :]
    return A 

def PLUinv(A):
    P, L, U = PLUDecompose(A)
    M = solve(L, P, lower=True)
    Ainv = solve(U, M, lower=False)
    return Ainv


def solve(A, B, lower): # 求解AX = B 其中A 是下三角矩阵
    N = A.shape[0]
    X = np.eye(N)
    for i in range(N):
        b = B[:, i]
        if lower:
            X[:, i] = lowersolution(A, b)
        else:
            X[:, i] = uppersolution(A, b)

    return X 

def uppersolution(A, b): # 求解 Ax = b （对于上三角矩阵，从最后一个开始求解，然后带入求解后续）
    n = len(b)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        tmp = (b[i] - (A[i, :] * x).sum())/A[i, i]
        x[i] = tmp
    
    return x 


def lowersolution(A, b): # 求解 Ax = b （对于下三角矩阵，从第一个开始求解，然后带入求解后续）
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        tmp = (b[i] - (A[i, :] * x).sum())/A[i, i]
        x[i] = tmp

    return x


if __name__ == '__main__':
    # A = np.array([[1,2,4,17], [3,6,-12,3], [2,3,-3,2],[0,2,-2,6]]).astype(np.float32)
    A = np.random.randint(0, 10, size=(3,3)).astype(np.float32)
    # A = np.array([[4,1],[0,1]]).astype(np.float32)
    M = np.linalg.inv(A)
    Ainv = PLUinv(A)
    print(Ainv)
    print(M)
    print((Ainv-M).sum() < 0.1)
