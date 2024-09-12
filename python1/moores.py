def findMajority(arr, n):
    candidate = -1
    votes = 0
     

    for i in range (n):
        if (votes == 0):
            candidate = arr[i]
            votes = 1
        else:
            if (arr[i] == candidate):
                votes += 1
            else:
                votes -= 1
    count = 0
     
    
    for i in range (n):
        if (arr[i] == candidate):
            count += 1
             
    if (count > n // 2):
        return candidate
    else:
        return -1
 

 
arr = [ 1, 1, 1, 1, 2, 3, 4 ]
n = len(arr)
majority = findMajority(arr, n)
print(" The majority element is :" ,majority)