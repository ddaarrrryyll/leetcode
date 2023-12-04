/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        if (list1 == null && list2 == null) return null;
        
        // merge into list1
        ListNode curr1 = list1;
        ListNode curr2 = list2;
        ListNode head = curr1;
        
        if (curr2.val < curr1.val) {
            head = curr2;
            curr2 = curr1;
            curr1 = head;
        }
        
        while (curr1.next != null && curr2 != null) {
            // if other node < my next node
            if (curr2.val < curr1.next.val) {
                ListNode temp1 = curr1.next;
                ListNode temp2 = curr2.next;
                curr1.next = curr2;
                curr2 = temp2; // update curr2
                curr1 = curr1.next; // update curr1
                curr1.next = temp1;
            } else {
                curr1 = curr1.next;
            }
        }
        if (curr1.next == null && curr2 != null) curr1.next = curr2;
        return head;
    }
}