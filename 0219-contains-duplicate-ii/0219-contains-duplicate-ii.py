class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lib = defaultdict(lambda: [])
        for i in range(len(nums)):
            checker = lib[nums[i]]
            if checker and i - checker[-1] <= k:
                return True
            lib[nums[i]].append(i)
        return False