def kadanes_algorithm(arr,n):
    max_sum =  float('-inf')
    curr_sum = 0
    for i in arr:
        curr_sum = max(curr_sum,0)
        curr_sum += i
        max_sum = max(curr_sum,max_sum)
        # if curr_sum > max_sum:
        #     max_sum = curr_sum
        # if curr_sum < 0:
        #     curr_sum = 0
    return max_sum





n = 5
arr = [1,2,3,-2,5]
print(kadanes_algorithm(arr,n))