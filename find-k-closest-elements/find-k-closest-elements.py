class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sol = []
        flag = 0

        # get index to start with
        mid = bisect.bisect(arr, x)
        right_i = mid
        left_i = mid-1
        try:
            right = arr[right_i]
        except:
            flag = 1
        left = arr[left_i]
        
        
        # follow conditions set by question, move left and right pointers accordingly
        while len(sol) < k:
            if flag == 1 or (left_i >= 0 and (left == x or (abs(left - x) < abs(right - x)) or (abs(left - x) == abs(right - x) and left < right))):
                bisect.insort(sol, left)
                left_i -= 1
                left = arr[left_i]
        
            else:
                bisect.insort(sol, right)
                try:
                    right_i += 1
                    right = arr[right_i]
                except:
                    flag = 1
                    
            # print(sol)
        return sol
                