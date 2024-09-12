class Solution:
    def factorial2(self,n):
        if n == 0 or n == 1:
           return 1
        else:
            return n * self.factorial2(n - 1)
        
    def factorial(self, N):
        fact = self.factorial2(N)
        fact_str = str(fact)  
        digits_list = [int(digit) for digit in fact_str]
        return digits_list