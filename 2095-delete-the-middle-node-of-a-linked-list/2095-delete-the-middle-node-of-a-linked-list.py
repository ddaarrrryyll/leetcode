# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None
        first, second, prev = head, head, head
        """
        f,x,x,x,x,x
        s,x,x,x,x,x
        
        x,f,x,x,x,x
        x,x,s,x,x,x
        
        x,x,f,x,x,x
        x,x,x,x,s,x
        """
        while second.next:
            prev = first
            first = first.next
            second = second.next.next if second.next.next else second.next
        if first.next:
            first.val = first.next.val
            first.next = first.next.next
        else:
            prev.next = None
        return head