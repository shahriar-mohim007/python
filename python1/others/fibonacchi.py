n = int(input("Enter a value for n: "))
fibonacci_list = [0, 1]

for i in range(2,n):
    sum = fibonacci_list[i-1]+fibonacci_list[i-2]
    fibonacci_list.append(sum)

print(fibonacci_list)

fibonacci_list = [0, 1]
while fibonacci_list[-1] + fibonacci_list[-2] <= n:
    next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
    fibonacci_list.append(next_fibonacci)

print("Fibonacci sequence up to", n, ":", fibonacci_list)
