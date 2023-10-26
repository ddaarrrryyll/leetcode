class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        MOD = 1000000007
        # start from the smallest number
        arr = sorted(arr)
        num_trees = {}
        for i in range(len(arr)):
            num = arr[i]
            num_trees[num] = 1
            for j in range(i):
                candidate = arr[j]
                if num % candidate == 0 and num // candidate in num_trees.keys():
                    num_trees[num] += num_trees[candidate] * num_trees[num//candidate]
        
        print(num_trees)
        
        return sum([v for k,v in num_trees.items()]) % MOD
            
            