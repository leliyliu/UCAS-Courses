import numpy as np 

if __name__ == '__main__':
    m, n = 5, 5
    matrix = np.random.randint(0, 20, size=(m,n)).astype(np.float32)
    data = np.random.randint(0, 20, size=(n, )).astype(np.float32)

    np.savetxt('matrix.csv', matrix)
    np.savetxt('data.csv', data)