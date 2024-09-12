# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5
nums = list(map(int, input().split()))
low = 0
high = len(nums)-1

while low<=high:
    if nums[low]>0 and nums[high]<0:
       nums[low],nums[high] = nums[high],nums[low]
       high-=1
       low+=1
    elif nums[low]>0 and nums[high]<0:
        nums[low],nums[high] = nums[high],nums[low]
        low+=1
        high-=1
    elif nums[low]<0:
        low+=1
    elif nums[high]>0:
        high-=1

print(nums)
         
low = 0
high = len(nums)-1

while low<=high:
    if nums[low]<0:
        low+=1
    elif nums[high]>0:
        high-=1
    else:
        nums[low],nums[high] = nums[high],nums[low]

print(nums)