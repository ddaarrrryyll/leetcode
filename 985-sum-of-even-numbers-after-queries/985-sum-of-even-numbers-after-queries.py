class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        out = deque()
        initial = sum([_ for _ in nums if _ % 2 == 0])
        out.append(initial)
        for idx in range(len(queries)):
            val, i = queries[idx]
            # nums[i] ends up being even from being even
            if val % 2 == 0 and nums[i] % 2 == 0:
                out.append(out[idx] + val)
            # nums[i] ends up being even from being odd
            elif val % 2 == 1 and nums[i] % 2 == 1:
                out.append(out[idx] + val + nums[i])
            # nums[i] ends up being odd from being even
            elif val % 2 == 1 and nums[i] % 2 == 0:
                out.append(out[idx] - nums[i])
            # nums[i] ends up being odd from being odd
            elif val % 2 == 0 and nums[i] % 2 == 1:
                out.append(out[idx])
                  
            nums[i] += val
            #print(nums, out)
            
        out.popleft()
        return out