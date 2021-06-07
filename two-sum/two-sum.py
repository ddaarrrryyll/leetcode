class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s_nums = sorted(nums)
        i = 0
        j = len(s_nums)-1
        head = s_nums[i]
        tail = s_nums[j]
        summ = head + tail
        print(s_nums)
        while summ != target and i < j:
            print(i, j)
            print(s_nums[i], s_nums[j], summ)
            if summ < target:
                i += 1
                head = s_nums[i]
            elif summ > target:
                j -= 1
                tail = s_nums[j]
            
            summ = head + tail
            
        else:
            print(head, tail)
            if nums.index(head) > nums.index(tail):
                temp = head
                head = tail
                tail = temp
            print(head, tail)
            return nums.index(head), nums.index(tail, nums.index(head)+1)