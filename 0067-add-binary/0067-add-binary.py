class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        c = a + b
        if c == 0: return '0'
        out = ""
        while c > 0:
            out = out + str(c % 2)
            c //= 2
        return out[::-1]