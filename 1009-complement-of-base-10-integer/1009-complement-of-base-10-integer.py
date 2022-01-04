class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # we can xor n with the maximum value given n's number of bits
        if n == 0: return 1
        bits = int(log(n, 2))+1
        max_val = 2 ** bits - 1
        
        return n ^ max_val