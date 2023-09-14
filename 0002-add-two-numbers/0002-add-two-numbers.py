# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l1_pointer = l1
        l2_pointer = l2
        temp = ListNode()
        res = temp
        while l1_pointer or l2_pointer:
            if not l1_pointer:
                l1_pointer = ListNode(0)
            if not l2_pointer:
                l2_pointer = ListNode(0)

            add = l1_pointer.val + l2_pointer.val + carry
            carry = 0
            if add >= 10:
                carry = 1
            temp.next = ListNode(add%10)
            temp = temp.next
            l1_pointer = l1_pointer.next
            l2_pointer = l2_pointer.next
        if carry == 1:
            temp.next = ListNode(1)
        return res.next