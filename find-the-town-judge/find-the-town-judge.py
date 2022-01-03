class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # everyone is assumed to be a judge at first
        judges = [1] * n
        
        # because a judge trusts no one, ai will mean that the person is not a judge, set to 0
        for pair in trust:
            judges[pair[0]-1] = 0
            
        # in the end, only one person will have 1
        # i.e. sum(judges) = 1, else return -1
        if sum(judges) == 1:
            
            # further check if everyone trusts the judge
            # count if n-1 people trusts the judge
            count = 0
            judge = judges.index(1)+1
            for pair in trust:
                if pair[1] == judge:
                    count += 1
            
            if count == n-1: return judge
            else: return -1 
        
        else:
            return -1