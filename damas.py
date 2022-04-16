class jogo:
    def __init__(self,n,m):
        campo = {}
        for i in range(n):
            for j in range(m):
                campo[(i,j)] = 0

        for j in range(0,m-1,2):
            campo[(0,j)] = 1
            campo[(7,j)] = 1
            campo[(1,j+1)] = 1
            campo[(6,j+1)] = 1

        jogo.campo = campo

    
A = jogo(8,8)
print(A.campo)