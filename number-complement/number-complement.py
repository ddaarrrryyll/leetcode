class Solution:
    def findComplement(self, num: int) -> int:
        # a number xor with the biggest representable integer (according to bits) will give its complement
        bits = int(log(num, 2)) + 1
        
        cap = 2**bits - 1
        return num ^ cap