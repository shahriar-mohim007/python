def palincheck(num):
    num =  str(num)
    left = 0
    right = len(num) -1
    
    while left<=right:
        if num[left] == num[right]:
           left+=1
           right-=1
        else:
            return False
    return True

def PalinArray(nums):
    for i in nums:
        if palincheck(i):
            continue
        else:
            return False
    
    return True



nums = list(map(int, input().split()))
print(nums)
print(PalinArray(nums))