# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # linked list is 1d, just need to keep track of visited
        # using a hashmap / default dict would keep runtime to minimum
        
        # second thought, change self.val to a char after visiting to keep memory O(1)
        ans = 0
        curr = head
        if not curr:
            return False
 
        curr.val = str(ans)
        
        while True:
            try:
                curr = curr.next
                if type(curr.val) != int:
                    # return int(curr.val); this returns pos lol 
                    return True
                else:
                    ans +=  1
                    curr.val = str(ans)
            except:
                break
        
        # return -1
        return False