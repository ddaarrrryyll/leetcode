class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_oc = {}
        first_oc[0] = 0
        answer = 0
        prefix = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                prefix += 1
            else:
                prefix -= 1
            if prefix in first_oc:
                answer = max(answer, i + 1 - first_oc[prefix])
            else:
                first_oc[prefix] = i + 1
        return answer