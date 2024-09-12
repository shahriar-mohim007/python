def longest_consecutive(nums):
     if not nums:
          return 0
     nums.sort()
     max_length = 1
     prev_element = nums[0]
     cur_length = 1

     for i in range(1,n):
         if nums[i] == prev_element+1:
              cur_length +=1
              max_length = max(cur_length,max_length)
         elif nums[i] != prev_element:
            cur_length = 1
        
         prev_element = nums[i]

     return max_length

def longestconsecutive(nums):
    numset1 = set(nums)
    maxi=1

    for i in numset1:
        if (i-1) not in numset1:
            next1 = i+1
            length = 1
            while next1 in numset1:
                next1 = next1 + 1
                length = length + 1
            maxi = max(maxi,length)
    return maxi


nums = [2,6,1,9,4,5,3,3]
n=len(nums)
print(longest_consecutive(nums))