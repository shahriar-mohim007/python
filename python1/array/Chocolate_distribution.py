def findMinDiff(nums,n,m):
    if m>n:
        return -1
    nums.sort()
    min_diff = float('inf')
    for i in range(n-m+1):
        diff = nums[i+m-1] - nums[i]
        min_diff = min(diff,min_diff)
    return min_diff

nums = list(map(int, input().split()))
n = len(nums)
m = int(input())
print(findMinDiff(nums,n,m))