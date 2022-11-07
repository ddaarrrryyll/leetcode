class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums = self.trimArr(nums)
        out = set()
        for i in range(len(nums)):
            complement = 0 - nums[i]
            pairs = self.findPairs(nums[i+1:], complement)
            for pair in pairs:
                out.add((nums[i], pair[0], pair[1]))
        return out
        
    
    def findPairs(self, nums: List[int], complement) -> List[List[int]]:
        out = []
        count = Counter(nums)
        mapper = defaultdict(lambda: None)
        for num in nums:
            pair = complement - num
            if pair != num or pair == num and count[num] > 1:
                mapper[pair] = num
        for num in nums:
            if mapper[num] != None:
                out.append(sorted([num, mapper[num]]))
            else:
                continue
        return list(out)
    
    def trimArr(self, nums: List[int]) -> List[int]:
        out = []
        count = Counter(nums)
        for k, v in count.items():
            out.extend([k for _ in range(min(v, 3))])
            
        return out