class Solution:
        
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        potential_mutations = collections.deque([[start,0]])
        visited = [start]
        if end not in bank: return -1
        if start == end: return 0
        

        while potential_mutations:
            curr, mutations = potential_mutations.popleft()
            
            if curr == end: return mutations

            for potential_mutation in bank:
                if self.differsByOne(curr, potential_mutation) and potential_mutation not in visited:
                    visited.append(potential_mutation)
                    potential_mutations.append([potential_mutation,mutations+1])
        return -1
    
        
    def differsByOne(self, curr: str, potential: str) -> bool:
        count = 0
        if curr == potential: return False
        for a, b in zip(curr, potential):
            if a!=b:
                if count: return False
                count += 1
        return True
    
    