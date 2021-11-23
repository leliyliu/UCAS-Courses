import numpy as np 

def lowertrinv(L): # 由于L矩阵的对角线元素均为1，所以直接利用其来实现约减 (下三角矩阵)
    N = L.shape[0]
    Linv = np.eye(N)
    matrix = np.copy(L)
    for i in range(N-1):
        for j in range(i+1, N):
            Linv[j, :] -= matrix[j,i] * Linv[i, :]
    
    return Linv

def uppertrinv(U): # 由于U的对角元素并不为1，所以要先做归一化处理 (上三角矩阵求逆)
    N = U.shape[0]
    Uinv = np.eye(N) 
    matrix = np.copy(U)
    for i in range(N):
        Uinv[i, :] = Uinv[i, :]/matrix[i, i]
        matrix[i, :] = matrix[i, :]/matrix[i,i]
    for i in range(N-1, -1, -1):
        for j in range(i-1, -1, -1):
            Uinv[j, :] -= matrix[j,i] * Uinv[i, :]
    
    return Uinv

def solve(matrixs, data, factorization_type):
    if(factorization_type=='LU'):
        P, L, U = matrixs
        Linv = lowertrinv(L)
        Uinv = uppertrinv(U)
        y = np.dot(P, data)
        tmp = Linv.dot(y)
        x = Uinv.dot(tmp)
        return x  
    elif(factorization_type=='QR'):
        Q, R = matrixs
        tmp = np.dot(Q.T, data)
        Rinv = uppertrinv(R)
        x = Rinv.dot(tmp)
        return x 
    else:
        P, T = matrixs 
        tmp = P.dot(data)
        Tinv = uppertrinv(T)
        x = Tinv.dot(tmp)
        return x 





