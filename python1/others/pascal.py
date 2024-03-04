def generate(n):
    result = []
    
    for i in range(n):
        row = [0] * (i + 1)
        row[0] = 1
        row[i] = 1

        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        
        result.append(row)
    
    return result

result= generate(5)

for i, list1 in enumerate(result):
    for _ in range(len(result) - i - 1):
        print(" ",end='')
    for i in list1:
        print(i,end=" ")
    print("\n")