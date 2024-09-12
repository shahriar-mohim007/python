def jump(arr,n):
    reachable = 0
    for i in range(n):
        if i>reachable:
            return False
        reachable = max(reachable,arr[i]+i)
    return True


def canJump(nums):
    length = len(nums)
    dp = [0] * length
    dp[0] = nums[0]
    
    for i in range(1, length - 1):
        if dp[i - 1] < i:
            return False
        
        dp[i] = max(i + nums[i], dp[i - 1])

        if dp[i] >= length - 1:
            return True
    
    return dp[0] >= length - 1