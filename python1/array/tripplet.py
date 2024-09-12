
def find3Numbers(nums,n,x): 
    nums.sort()
    for i in range(n-2):
        left = i+1
        right = n-1
        
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == x:
                return True
            elif sum<x:
                left += 1
            else:
                right -= 1
        
        return False


nums = list(map(int, input().split()))
n = len(nums)
x = int(input())
print(find3Numbers(nums,n,x))