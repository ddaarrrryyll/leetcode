class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                days_to_today = idx - stack[-1]
                res[stack.pop()] = days_to_today
                
            stack.append(idx)
        return res