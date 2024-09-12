def threeWayPartition(arr, low, high):
    i = 0
    mid = 0
    n = len(arr)-1

    while mid <= n:
        if arr[mid] < low:
            arr[i], arr[mid] = arr[mid], arr[i]
            i += 1
            mid += 1
        elif low <= arr[mid] <= high:
            mid += 1
        else:
            arr[mid], arr[n] = arr[n], arr[mid]
            n -= 1
            
    
    return arr


nums = list(map(int, input().split()))
a,b = map(int, input().split())
print(threeWayPartition(nums,a,b))