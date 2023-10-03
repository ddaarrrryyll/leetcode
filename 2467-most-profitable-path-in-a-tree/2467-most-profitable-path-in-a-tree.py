class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # create adj list
        adjList = defaultdict(list)
        for u,v in edges :
            adjList[u].append(v)
            adjList[v].append(u)

        n = len(adjList)
        # create a time array to see which node bob reaches at which time
        time = [0]*n
        time[bob] = 1

        # dfs to backtrack how long it takes for bob to reach root
        def dfs1(node, prev):
            # base case we reach where bob is
            if node == bob :
                return time[bob]
            
            res = 0
            # traverse each neighbour
            for neighbour in adjList[node]:
                if neighbour == prev:
                    continue
                dist_to_prev = dfs1(neighbour, node)
                # if not 0, means can reach there from bob's position
                if dist_to_prev != 0  :
                    res = 1 + dist_to_prev
            # update the result to reach node
            time[node] = res
            return time[node]
        dfs1(0, None)


        self.res = float("-inf")
        
        # dfs for alice
        def dfs2(node, prev, t, income):
            for neighbour in adjList[node]:
                # go back
                if neighbour == prev :
                    continue
                # update time
                newTime = t + 1
                newIncome = income
                # if B never reached neighbour or A reaches neighbour before B we take the value
                if time[neighbour] == 0 or newTime < time[neighbour] :
                    newIncome += amount[neighbour]
                # if we reach same time, we split
                elif newTime == time[neighbour] :
                    newIncome += amount[neighbour]//2
                # if neighbour is the leaf node, we compare with what results we have and take the max one
                if len(adjList[neighbour]) == 1 :
                    self.res = max(self.res, newIncome)
                # move on to dfs neighbour
                dfs2(neighbour, node, newTime, newIncome)


        dfs2(0, None, 1, amount[0])
        return self.res
        