def selling_share(nums,n):
    profit = [0]*n

    max_price = nums[n-1]
    for i in range(n-2,0,-1):
        if nums[i] > max_price:
            max_price = nums[i]

        profit[i] = max(profit[i+1],max_price-nums[i])
    
    min_price = nums[0]

    for i in range(1,n):
        if nums[i]<min_price:
            min_price = nums[i]
        

        profit[i] = max(profit[i-1],profit[i]+(nums[i]-min_price))
     
    return profit[n-1]
nums = list(map(int, input().split()))
n = len(nums)
print(selling_share(nums,n))