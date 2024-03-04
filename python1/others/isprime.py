# def is_prime(number):
#     if  number<=1:
#         return False

#     sqrt_number = int(number**0.5)+1

#     for i in range(2,sqrt_number):
#         if number%i==0:
#             return False
        
#     return True

def generate_prime_in_range(end_num):
    flag_prime_or_not = [True]*(end_num+1)
    flag_prime_or_not[0]=flag_prime_or_not[1]=False
    n_root = int(end_num**0.5)+1
    for num in range(2,n_root):
        if flag_prime_or_not[num]:
            for i in range(num*num,end_num+1,num):
                    flag_prime_or_not[i] = False
    return flag_prime_or_not

def is_prime(i):
    if flag_prime_or_not[i]:
       return True
    else:
        return False

a, b = map(int, input("Enter two numbers: ").split())
flag_prime_or_not = generate_prime_in_range(b)

for i in range(a,b+1):
    if is_prime(i):
        print(f'{i} is a prime Number')
    else:
        print(f'{i} is a Not a prime Number')