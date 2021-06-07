class Solution:
    def isHappy(self, n: int) -> bool:
        count = 1
        vals = {n}
        
        while True:
            num = str(n)
            result = 0
            for i in num:
                result += int(i) ** 2
                
            if count == len(vals):
                n = result
                count += 1
                vals.add(result)
                continue
            
            else: 
                if result == 1:
                    return True
                return False