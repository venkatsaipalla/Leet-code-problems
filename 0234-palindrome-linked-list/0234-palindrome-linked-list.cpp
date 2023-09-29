/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* temp){
        
        ListNode *nxt;
        ListNode *prev=NULL;
        while(temp!=NULL){
            nxt=temp->next;
            temp->next=prev;
            prev=temp;
            temp=nxt;
        }
        return prev;
    }
    bool isPalindrome(ListNode* head) {
        if(head==NULL or head->next==NULL){
            return true;
        }
        ListNode *fast=head;
        ListNode *slow = head;
        ListNode *dummy=head;
        while(fast->next!=NULL and fast->next->next!=NULL){
            fast=fast->next->next;
            slow=slow->next;
        }
        slow->next=reverseList(slow->next);
        slow=slow->next;
        // ListNode* x=slow;
        // while(x!=NULL){
        //     cout<<x->val;
        //     x=x->next;
        // }
        // cout<<endl;
        while(slow!=NULL){
            // cout<<slow->val<<" mm"<<endl;
            if(slow->val!=dummy->val){
                return false;
            }
            dummy=dummy->next;
            slow=slow->next;
        }
        return true;
    }
};