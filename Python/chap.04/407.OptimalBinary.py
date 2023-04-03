def optsearchtree(p):
    n = len(p)-1
    A = [[-1]*(n+1) for _ in range(n+2)]
    R = [[-1]*(n+1) for _ in range(n+2)]
    for i in range(1, n+1):
        A[i][i-1] = 0
        A[i][i] = p[i]
        R[i][i-1] = 0
        R[i][i] = i
    A[n+1][n] = 0
    R[n+1][n] = 0
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i+diagonal
            A[i][j], R[i][j] = minimum(A, p, i, j)
    return A, R
