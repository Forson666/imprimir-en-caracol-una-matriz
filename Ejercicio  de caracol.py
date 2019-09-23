def transpuesta(mat):
    matT = []
    for j in range(len(mat[0])):
        fil = []
        for i in range(len(mat)):
            fil += [mat[i][j]]
        matT.append(fil)
    return matT

def girar(mat):
    mat = transpuesta(mat)
    mat.reverse()
    return mat
    
def caracol(mat):
    if len(mat) == 1:
        return mat[0]
    elif len(mat) > 1:
        return mat[0] + caracol(girar(mat[1:]))

print(caracol([[1,2,3],[4,5,6],[7,8,9]]))
