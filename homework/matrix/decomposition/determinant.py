import numpy as np 

def upperdet(matrix): # 计算上三角矩阵的行列式值，也就是对角线元素相乘
    """
    :param matrix: 输入矩阵
    :param det: 行列式的值
    """
    det = 1 
    N = matrix.shape[0]
    for i in range(N):
        det = det * matrix[i,i]
    return det 

def ReversedOrder(matrix): # 计算逆序对的数量，并根据结果，输出1或者-1 
    """
    :param matrix: 输入矩阵
    :param num: 逆序对数量对应的最终结果
    """
    orders = np.where(matrix==1)[1]
    count = 0
    for i, num in enumerate(orders):
        for j in range(i):
            if num < orders[j]:
                count += 1  
    return -1 if count%2 else 1 
