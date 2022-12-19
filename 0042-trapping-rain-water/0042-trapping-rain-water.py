class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        l_max, r_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= l_max:
                    l_max = height[left]
                else:
                    ans += l_max - height[left]
                left += 1
            else:
                if height[right] >= r_max:
                    r_max = height[right]
                else:
                    ans += r_max - height[right]
                right -= 1
                
        return ans