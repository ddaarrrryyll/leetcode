class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        
        state = [0] * numCourses
        
        def cycled(v):
            if state[v] == 1: return False
            if state[v] == -1: return True
            
            state[v] = -1
            for i in adjList[v]:
                if cycled(i): return True
            
            state[v] = 1
            return False
        
        for v in range(numCourses):
            if cycled(v): return False
        return True