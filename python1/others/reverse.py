input_string = list(input())
start,end=0,len(input_string)-1

while start<end:
    input_string[start],input_string[end] = input_string[end],input_string[start]
    start+=1
    end-=1

print(''.join(input_string))


