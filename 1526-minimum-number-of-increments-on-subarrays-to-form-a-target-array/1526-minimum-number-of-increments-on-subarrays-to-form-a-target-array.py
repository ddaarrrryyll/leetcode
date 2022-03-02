class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # smaller value between two larger values divides the target array into sub arrays eg 3,1,5,4,2
        # 1 divides array into 3 and 5,4,2, left sub array requires min 3 operations, right sub array requires min 5 operations
        # if we count the operation required for the pivot during the operation required for 3, we can use
        # 1 (to increment pivot) + 2 (to increment left sub array) + 4 (to increment right sub array)
        
        # this can also be seen to work by taking the first element as the min, and then incrementing answers whenever we meet an element
        # larger than the previous which acts as the pivot
        
        # len of target >= 1
        ans = target[0]
        
        if len(target) != 1:
            for i in range(1, len(target)):
                if target[i] > target[i-1]:
                    ans += target[i]-target[i-1]
                    
        return ans