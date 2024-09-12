def subset(nums1,nums2):
    map1 = {}
    map2 = {}

    for i in nums1:
        map1[i] = map1.get(i,0) + 1

    for num in nums2:
        map2[num] = map2.get(num, 0) + 1

    print(map1)
    print(map2)
    for num, count in map2.items():
        if num not in map1 or map1[num] < count:
            return False
        
    return True





nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(subset(nums1,nums2))