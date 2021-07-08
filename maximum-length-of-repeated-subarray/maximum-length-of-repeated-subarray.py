# using an altered form of sliding window, we try to find the first occurence of a repeated element, once we found the repeating element, we can increase the size of our window and 
# start from the index of the first occurence
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        sol = 0
        start = 0
        flag = 0
        for right in range(len(nums1)+1):
            for left in range(start, len(nums1)):
                # if left == start:
                #     print(f"starting from {start} for window of size {sol}")
                    
                # if left + right > len(nums1) we overshot then we need to go to the next size    
                if left + right <= len(nums1):
                    window = nums1[left:left+right]
                    # print(window)
                    if self.helper(window, nums2):
                        if window == nums2:
                            return sol
                        # print(f"found {window = }")
                        # set next starting point as the first place we found similarity and break from inner for loop
                        start = left
                        break
                    
                    # if we reached the last element without breaking then there are no duplicates => return 0 (only happens for size = 1) 
                    if left == len(nums1)-1:
                        return 0
                    
                else:
                    flag = 1
                    break
                
                    
            if flag == 1:
                sol-=1
                break
            else:
                sol+=1
                
        return sol
        
        
        
    def helper(self, A, X):
        for i in range(len(X) - len(A) + 1):
            if A == X[i:i+len(A)]: return True
        return False
