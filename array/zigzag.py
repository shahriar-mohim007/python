
def fill_zigzag_matrix(matrix, n):
    num = 1
    for layer in range(0,(n+1)//2):
        for i in range(layer,n-layer):
            matrix[layer][i] = num
            num += 1
        for i in range(layer+1,n-layer):
            matrix[i][n-layer-1] = num
            num += 1
        for i in range(n-layer-2,layer-1,-1):
            matrix[n-layer-1][i] = num
            num += 1
        for i in range(n-layer-2,layer,-1):
            matrix[i][layer] = num
            num += 1

n = int(input("Enter size of the matrix: "))
matrix = [[0 for _ in range(n)] for _ in range(n)]
fill_zigzag_matrix(matrix, n)
for row in matrix:
    print(row)