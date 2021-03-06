class Solution:
    def grayCode(self, n: int) -> List[int]:
        # print(f"n = {n}")
        if n == 1:
            return [0,1]
        else:
            l = self.grayCode(n - 1)
            
            # msb in dec
            msb = 2 ** (n-1)
            # print(f"msb = {msb}")
            # start from back, add msb value to each dec int
            i = len(l) - 1
            while i >= 0:
                l.append(l[i] + msb)
                i-=1
                # print(l)
        return l

"""
stdout for n = 4:

n = 4
n = 3
n = 2
n = 1
msb = 2                                            msb
[0, 1, 3] --------------[0, 1, 1+2] // [00, 01, 01+10] msb
[0, 1, 3, 2]------------------------// [00, 01, 11, 00+10]
msb = 4
[0, 1, 3, 2, 6]
[0, 1, 3, 2, 6, 7]
[0, 1, 3, 2, 6, 7, 5]
[0, 1, 3, 2, 6, 7, 5, 4]
msb = 8
[0, 1, 3, 2, 6, 7, 5, 4, 12]
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13]
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15]
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14]
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10]
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11]
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9]
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
"""
