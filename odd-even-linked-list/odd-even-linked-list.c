/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* oddEvenList(struct ListNode* head){
    int len = 0;
    struct ListNode *temp = head;
    while (temp) {
        len ++;
        temp = temp->next;
    }
    if (len < 3) return head;
    // 1, 2, 3, 4 ,5
    // 1
    struct ListNode *odd = head;
    // 2
    struct ListNode *even = odd->next;

    // 3
    
    struct ListNode *aft_even = even->next;
    struct ListNode *aft_odd;
    
    // to join with end of odd
    temp = head->next;
    
    int i;
    
    for (i = 0; i < len; i++) {
        // odd index i % 2 = 0
        // 1, 2, 3, 4, 5
        
        // printf("%d, %d\n", odd->val, even->val);
        if (i % 2 == 0) {
            // 1->3 | 3->5
            odd->next = aft_even;
            if (odd->next) {
                // 3 | 5
                odd = odd->next;
                // 4 | None
                aft_odd = odd->next;
            } else aft_odd = NULL;
        } else {
            // 2->4 | 4->NULL
            even->next = aft_odd;
            if (even->next) {
                // 4
                even = even->next;
                // 5
                aft_even = even->next;
            } else aft_even = NULL;  
        }
    }
    
    odd->next = temp;
    return head;
}