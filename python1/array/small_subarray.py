def smallestSubWithSum(nums,a):
    i = 0
    mid = 0
    high = len(nums) - 1
    sum = 0
    ans = float("INF")
    while mid<=high:
        sum+= nums[mid]
        mid+=1
        
        if sum > a:
            while sum>a:
                sum-=nums[i]
                i+=1
                ans = min(ans,mid-i+1)
            
    if ans == float("INF"):
        return 0
    return ans




nums = list(map(int, input().split()))
a = int(input())
print(smallestSubWithSum(nums,a))