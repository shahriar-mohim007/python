def more_than_n(arr,n,k):
    x = n//k

    freq = {}

    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    result = []
    for key, value in freq.items():
        if value > x:
            result.append(key)

    return result


arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
n = len(arr)
k = 4
print(more_than_n(arr, n, k))