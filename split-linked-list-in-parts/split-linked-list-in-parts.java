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
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode[] out = new ListNode[k];
        int size = getlength(head);
        // if size < k, the first size array will only have 1 element
        if (size < k) {
            fill(head, out, 0, size, 1);
        } else {
            // minimum size of arrays
            int min = size / k;
            // number of bigger size arrays
            int x = size % k;
            // fill first x arrays
            head = fill(head, out, 0, x, min+1);
            // fill remaining k-x arrays
            head = fill(head, out, x, k, min);
        }
        return out;
    }
    
    private ListNode fill(ListNode head, ListNode[] out, int first, int last, int size) {
        for (int i = first; i < last && head != null; i++) {
            out[i] = head;
            for (int j = 0; j < size-1 && head != null; j++) head = head.next;
            // create new listnode
            if (head != null) {
                ListNode temp = head.next;
                head.next = null;
                head = temp;
            }
        }
        return head;
    }
    
    private int getlength(ListNode head) {
        int l = 0;
        while (head != null) {
            l++;
            head = head.next;
        }
        return l;
    }
}