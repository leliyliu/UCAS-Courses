import numpy as np 
import argparse 

from decomposition import PLUFactorization, QRFactorization, HouseholderReduction, GivensReduction, URVFactorization
from solution import solve
from determinant import upperdet, ReversedOrder

Factorization_Choices =['LU', 'QR', 'Householder', 'Givens', 'URV']

parser = argparse.ArgumentParser(description='Args for matrix factorization')
parser.add_argument('-f', '--factorization', type=str, default='URV', choices=Factorization_Choices)
parser.add_argument('-p','--path', type=str, default='matrix.csv')
parser.add_argument('--solve', default=False, action='store_true')
parser.add_argument('-d', '--data', type=str, default='data.csv')
parser.add_argument('--determinant', default=False, action='store_true')
args = parser.parse_args()

np.set_printoptions(precision=3, suppress=True) #设置小数位置为3位

def read_data(path):
    matrix = np.loadtxt(path)
    return matrix 

if __name__ == '__main__':
    matrix = read_data(args.path)
    print(matrix)
    if(args.factorization == 'LU'):
        matrixs = PLUFactorization(matrix)
        print('----------the LU FACTORIZATION RESULTS----------')
        print('P')
        print(matrixs[0])
        print('L')
        print(matrixs[1])
        print('U')
        print(matrixs[2])
        print('original results')
        print(np.dot(matrixs[1],matrixs[2]))
    elif(args.factorization == 'QR'):
        matrixs = QRFactorization(matrix)
        print('----------the QR FACTORIZATION RESULTS----------')
        print('Q')
        print(matrixs[0])
        print('R')
        print(matrixs[1])
        print('original results')
        print(np.dot(matrixs[0],matrixs[1]))
    elif(args.factorization == 'Householder'):
        matrixs = HouseholderReduction(matrix)
        print('----------the HOUSEHOLDER REDUCTION RESULTS----------')
        print('P')
        print(matrixs[0])
        print('T')
        print(matrixs[1])
        print('original results')
        print(np.dot(matrixs[0].T,matrixs[1]))
    elif(args.factorization == 'Givens'):
        matrixs = GivensReduction(matrix)
        print('----------the GIVENS REDUCTION RESULTS----------')
        print('P')
        print(matrixs[0])
        print('T')
        print(matrixs[1])
        print('original results')
        print(np.dot(matrixs[0].T,matrixs[1]))
    else:
        matrixs = URVFactorization(matrix)
        print('----------the URV FACTORIZATION RESULTS----------')
        print('U')
        print(matrixs[0])
        print('R')
        print(matrixs[1])
        print('V')
        print(matrixs[2])
        print('original results')
        print(np.dot(np.dot(matrixs[0],matrixs[1]), matrixs[2].T))

    if args.solve:
        data = read_data(args.data)
        print('----------b----------')
        print(data)
        if(args.factorization == 'URV'):
            matrixs = HouseholderReduction(matrix)
        x = solve(matrixs, data, args.factorization)
        print('----------x: equation results----------')
        print(x)

    if args.determinant:
        assert(matrix.shape[0] == matrix.shape[1]), "Error! Only square matrix available for determinant computation"
        if(args.factorization == 'LU'):
            P, _, U = matrixs
        else:
            P, _, U  = PLUFactorization(matrix)

        delta = ReversedOrder(P)
        det = delta * upperdet(U)
        print('-----------det value------------')
        print(det)
        

