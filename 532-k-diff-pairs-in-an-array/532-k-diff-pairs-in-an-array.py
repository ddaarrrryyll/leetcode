class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # sort nums, then iterate with a dict
        nums.sort()
        # print(nums)
        ans = []
        pair = defaultdict(lambda: num+k)
        
        for num in nums:
            # preventing duplicates
            if num in pair.values() and (num, num-k) not in ans:
                ans.append((num, num-k))
            pair[num]
        #  print(pair)
        # print(ans)
        return len(ans)