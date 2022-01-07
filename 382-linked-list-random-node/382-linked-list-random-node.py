# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        ans = 0
        sample_size = 1
        node = self.head
        while node:
            # random() gives a value between 0 and 1 with equal probability
            if random.random() < 1 / sample_size:
                ans = node.val
            node = node.next
            sample_size += 1
            
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()