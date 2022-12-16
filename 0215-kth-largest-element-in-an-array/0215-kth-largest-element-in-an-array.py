class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def countingSort(nums):
            min_val = min(nums)
            delta = abs(min_val)
            for i, num in enumerate(nums):
                nums[i] += delta # this gives the position that the current number is supposed to be at and accounts for missing numbers in between
            # print(nums)
            max_val = max(nums)
            counter = Counter(nums)
            sorted_nums = []
            for i in range(max_val + 1):
                if i in counter:
                    # i-delta is the original number, counter[i] is the number of times to put the original number in
                    # print([i-delta] * counter[i])
                    sorted_nums += [i-delta] * counter[i]
            return sorted_nums
        nums = countingSort(nums)
        # print(nums)
        return nums[-k]
        