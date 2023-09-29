/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        // if(head and head->next){
        //     return head;
        // }
        ListNode *slow=head;
        ListNode *fast=head;
        ListNode *temp=head;
        while(fast and fast->next){
            fast=fast->next->next;
            slow=slow->next;
            if(slow==fast){
               while(slow!=temp){
                temp=temp->next;
                slow=slow->next;
               }
                return temp;
            }
        }
        
        return nullptr;
        
    }
};