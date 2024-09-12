def trappingWater(arr,n):
    left = 0
    right = n-1
    left_max = right_max = 0
    water_trapped = 0
    while left<right:
        if arr[left]<=arr[right]:
            if arr[left]>=left_max:
                left_max = arr[left]
            else:
                water_trapped+=left_max-arr[left]
            
            left += 1
        else:
            
            if arr[right]>=right_max:
                right_max = arr[right]
            else:
                water_trapped+=right_max-arr[right]
                print(arr[right],right_max,water_trapped)
            
            right-=1
    
    return water_trapped




nums = list(map(int, input().split()))
n = len(nums)
print(trappingWater(nums,n))