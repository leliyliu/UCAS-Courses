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
        # print('STEP ', i+1, '   ', pivot)
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
    Uinv = uppertrinv(U)
    Linv = lowertrinv(L)
    ULinv = matmul(Uinv, Linv)
    return matmul(ULinv, P)

def lowertrinv(L): # 由于L矩阵的对角线元素均为1， 所以直接利用其来实现约减
    N = L.shape[0]
    Linv = np.eye(N)
    for i in range(N-1):
        for j in range(i+1, N):
            Linv[j, :] -= L[j,i] * Linv[i, :]
    
    return Linv

def uppertrinv(U): # 由于U的对角元素并不为1， 所以要先做归一化处理
    N = U.shape[0]
    Uinv = np.eye(N)
    for i in range(N):
        Uinv[i, :] = Uinv[i, :]/U[i, i]
        U[i, :] = U[i, :]/U[i,i]
    for i in range(N-1, -1, -1):
        for j in range(i-1, -1, -1):
            Uinv[j, :] -= U[j,i] * Uinv[i, :]
    
    return Uinv

def matmul(A,B): # 由于都是方阵，这里只实现方阵的乘法 
    N = A.shape[0]
    out = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                out[i,j] += A[i, k]*B[k, j]
    return out 

if __name__ == '__main__':
    # A = np.array([[1,2,4,17], [3,6,-12,3], [2,3,-3,2],[0,2,-2,6]])
    A = np.random.randint(0, 10, size=(3,3)).astype(np.float32)
    # A = np.array([[4,1],[0,1]]).astype(np.float32)
    print(A)
    M = np.linalg.inv(A)
    print(A)
    Ainv = PLUinv(A)
    print(Ainv)
    print(M)
    print((Ainv-M).sum() < 0.1)
