list1 = [1,2,3,4,5]

list2 = list1
list2[0] = 1000
print(list1)
size = len(list1)

for i in range(size-1,-1,-1):
    print(list1[i],end='')

print('\n')

print(list1[:-1])
print(list1[-5:])
a = [1,2,3,4,5,6]
print(a[len(a):-len(a)-1:-1])

