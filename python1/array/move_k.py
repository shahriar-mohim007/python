# A simple solution is to first count all elements less than or equal to k(say ‘good’). 
# Now traverse for every sub-array and swap those elements whose value is greater than k. The time complexity of this approach is O(n2)
def min_swaps_naive(arr, n, k):
    count = 0
    for i in range(n):
      if arr[i] <= k:
        count += 1

    swaps = 0
    ans  = float('INF')
    for i in range(n-count+1):
      swaps = 0
      for j in range(i, i+count):
        if arr[j] > k:
          swaps += 1
      

      
      ans = min(ans,swaps)
    
    if ans == float('INF'):
      return 0

    return ans

def min_swap(arr,n,k):
    count = 0
    for i in range(n):
        if arr[i] <= k:
          count += 1
    bad = 0
    for i in range(0,count):
      if arr[i]>k:
        bad += 1

    ans = bad
    j = count
    for i in range(0,n):
        if(j == n) :
           break
        
        if (arr[i] > k) :
            bad = bad - 1
          
        if (arr[j] > k) :
            bad = bad + 1
          
        ans = min(ans, bad)
  
        j = j + 1
      
    return ans


arr = [19,9]
k = 18
min_swaps = min_swap(arr, len(arr), k)
print("Minimum swaps required:", min_swaps)
