import  numpy as np
from numpy.linalg import matrix_rank, norm
np.set_printoptions(precision=3) #设置小数位置为3位

def change_row(matrix,i,j):
    '''
    :param matrix: 输入矩阵
    :param i，j:需交换的行
    :return： 交换后的矩阵
    '''
    matrix[[i,j], :] =  matrix[[j,i], :]
    return matrix

def PLUFactorization(matrix):
    '''
    :param matrix: 输入矩阵
    :param P L U: 分解得到的输出矩阵
    '''
    # print("----------------------- input :-----------------------")
    # print(matrix)
    U = np.copy(matrix)
    row_len=U.shape[0]
    col_len=U.shape[1]

    assert (row_len == col_len), "PLU Factorization needs a square matrix"
    P, L = np.eye(row_len), np.zeros((row_len,row_len)) # P 初始化一个 I 矩阵，L矩阵初始化为一个0矩阵

    for i in range(row_len):
        j = np.argmax(abs(U[i:, i])) + i  # 找到当前列的从i开始的最大值，然后进行交换
        U = change_row(U, i, j)
        P = change_row(P, i, j) # 同样的，需要对P和L 进行行交换
        L = change_row(L, i, j)
        pivot = U[i,i] # 保存主元
        assert(pivot!=0), "Error! a zero pivot is encoutered"
        for k in range(i,row_len):
            L[k,i] = U[k,i]/pivot
        for m in range(i+1,row_len):
            for n in range(i+1,row_len):
                U[m,i] = 0
                U[m,n] -= L[m,i] * U[i, n]

    return P, L, U  # 这里的matrix经过变化，已经处理为U 

def check(matrix):# 判断QR分解的矩阵条件：所有列线性无关，即矩阵秩=列数
    rank = matrix_rank(matrix)
    n=matrix.shape[-1]
    return rank == n

def QRFactorization(matrix): # QR 分解 
    '''
    :param matrix: 输入矩阵
    :return: 正交矩阵Q，上三角矩阵R
    '''
    assert(check(matrix)), "Error! Not all columns in matrix are linearly independent"
    Q = np.zeros_like(matrix)
    for index, a in enumerate(matrix.T):
        u = np.copy(a)
        for i in range(index):
            u=u-np.dot(np.dot(Q[:, i].T,a), Q[:, i]) #减去分量
        norm_factor=norm(u) #归一化
        Q[:, index]=u/norm_factor
    R = np.dot(Q.T,matrix)
    return Q, R

def HouseholderReduction(matrix):# Householder 约减 (为了简便，这里只考虑实数，所以设u为1)
    '''
    :param matrix: 输入矩阵
    :return: 正交矩阵P， 上三角矩阵T
    '''
    row_len=matrix.shape[0]
    P = np.identity(row_len)
    T = np.copy(matrix)
    for index in range(row_len - 1):
        a = T[index:, index]
        u = np.copy(a)
        norm_factor=norm(a) # 归一化因子
        u[0] -= norm_factor # 矩阵列向量-归一化因子*单位向量(变换构造第一二步)
        u = u.reshape(-1, 1)
        R=2.0*(np.dot(u, u.T))/(u.T.dot(u)) 
        I = np.identity(row_len)
        I[index:, index:] -= R # 得到对应的R 变为 I-2uu.T/u.Tu
        T = np.dot(I, T)
        P = np.dot(I, P)

    return P, T

def GivensReduction(matrix): # givens 分解
    '''
    :param matrix: 输入矩阵
    :return: 正交矩阵P， 上三角矩阵T
    '''
    row_len = matrix.shape[0]
    col_len = matrix.shape[1]
    P = np.identity(row_len)
    T = np.copy(matrix)
    for i in range(row_len):
        for j in range(col_len-1,i,-1):
            val_a=T[i,i]
            val_b=T[j,i]
            mag = np.sqrt( (val_a ** 2 + val_b ** 2) )
            c = val_a / mag
            s = val_b / mag
            Pi = np.eye(row_len)
            Pi[i, i] = c
            Pi[j, j] = c
            Pi[i, j] = s
            Pi[j, i] = -s
            P = np.dot(Pi,P)
            T = np.dot(Pi,T)

    return P, T

def URVFactorization(matrix):#URV分解
    '''
    :param matrix: 需分解的矩阵
    :return: m*m的正交矩阵U，V为n*n的正交矩阵V R为m*n的矩阵
    '''
    P1, T1 = HouseholderReduction(matrix)
    U = P1.T
    temp = T1[:matrix_rank(T1), :] # n*n
    P2,T2 = HouseholderReduction(temp.T)
    V = P2.T
    T = T2[:matrix_rank(T2), :]
    R = np.zeros_like(matrix,dtype=float)
    R[:matrix_rank(T2), :matrix_rank(T2)] = T.T

    return U, R, V



