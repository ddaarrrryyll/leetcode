class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        
        # n = a + a+1 + a+2 + ...
        # n - (1+2+3+...) ie n - const must be divisible by x (number of consecutive numbers)
        
        out = 0
        
        # x is the number of consecutive numbers, start from 1 to show n is a consecutive number of itself, n//2 + 2 to include n//2 + 1
        for x in range(1, n//2 + 2):
            # formula for sum from 1 to x-1
            const = (x * (x-1)/2)
            if const >= n:
                break
            if (n-const) % x == 0:
                out += 1
        return out
        
# TLE D:
# class Solution:
#     def consecutiveNumbersSum(self, n: int) -> int:
#         # formula for sum of AP: 
#         # n = x/2 * (2a + x-1)
#         # 2n = 2ax + x^2 - x
#         # 2n = (2a-1)x + x^2
#         # x^2 + (2a-1)x - 2n = 0
        
#         # max value for a = n // 2 because for n = 7, if a=4, a+1 = 5, a+a+1 = 9 (overshot)
#         # i think n itself counts as a consecutive number
#         out = 1
#         # first number in consecutive
#         for a in range(1, n//2 + 1):
#             # if we can solve the quadratic equation, we add 1 to the number of ways
#             if self.solver(1, 2*a-1, -2*n):
#                 out += 1
    
#         return out
    
#     # function to solve quadratic equations in the form a*x^2 + b*x + c
#     def solver(self, a, b, c):
#         # print(f"solving {a}x^2 + {b}*x + {c}")
#         try:
#             # only need to find the positive one
#             x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
#         except ValueError:
#             print("complex number")
#             return False
        
#         # x1 = number of consecutive from a
#         # so if x1 > 0 (check again) and x1 is integer, return true
#         if x1 > 0 and x1.is_integer():
#             # print(x1, x2)
#             return True
    