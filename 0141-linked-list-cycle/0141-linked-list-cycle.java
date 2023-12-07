/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode fast = head.next;
        ListNode slow = head;
        
        while (slow != null && fast != null) {
            
            if (slow == fast) return true;
            
            slow = slow.next;
            if (fast.next != null) fast = fast.next.next;
            else return false;
        }
        
        return false;
    }
}