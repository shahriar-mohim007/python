def rotate_one_position(arr,n):
    last = arr[n-1]
    for i in range(n-1,-1,-1):
        arr[i] = arr[i-1]

    arr[0] = last
    return arr

n = 8
arr = [9, 8, 7, 6, 4, 2, 1, 3]
print(rotate_one_position(arr=arr,n=n))