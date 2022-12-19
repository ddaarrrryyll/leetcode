class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # https://youtu.be/eCaXlAaN2uE?t=437
        """
        Lets f(n) is a function which is set of valid string with n (matched) parantheses.
        f(0) = ‘’
        f(1) = (f(0))f(0)
        f(2) = (f(0))f(1) + (f(1))f(0)
        f(3) = (f(0))f(2) + (f(1))f(1) + (f(2))f(0)
        
        In general
        
        f(n) = ( f(0) ) f(n-1) + ( f(1) ) f(n-2) + ( f(2) ) f(n-3) + ...... + ( f(n-1) ) f(0)
        """
        
        parens = [[] for _ in range(n+1)]
        
        # base case
        parens[0] += '',
        for i in range(1,n+1):
            for j, k in zip(range(i), reversed(range(i))):
                for x in parens[j]:
                    for y in parens[k]:
                        parens[i].append(f'({x}){y}') 
                
        return parens[-1]