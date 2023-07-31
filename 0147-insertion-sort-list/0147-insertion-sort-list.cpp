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
    ListNode* insertionSortList(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr =head;
        ListNode* prev = dummy;
        prev->next=head;
        while(curr!=NULL){
            if(curr->next!=NULL && curr->next->val < curr->val){
                while(prev->next!=NULL && prev->next->val < curr->next->val){
                    prev=prev->next;
                }
                ListNode* temp=prev->next;
                prev->next=curr->next;
                curr->next=curr->next->next;
                prev->next->next=temp;
                prev=dummy;
            }else{
                curr=curr->next;
            }
        }
    
        return dummy->next;
          
}};

// class Solution {
// public:
//     ListNode* insertionSortList(ListNode* head) {
//       ListNode* dummy = new ListNode(0);
//       ListNode* curr = head;
//       ListNode* prev = dummy;
//       prev->next = head;
//       while(curr!=NULL){
//           if(curr->next!=NULL && curr->next->val<curr->val){
//               while(prev->next!=NULL && prev->next->val<curr->next->val){
//                   prev=prev->next;
//               }
//               ListNode* temp=prev->next;
//               prev->next = curr->next;
//               curr->next = curr->next->next;
//               prev->next->next = temp;
//               prev = dummy;
//           }
//           else{
//               curr=curr->next;
//           }
//       }
//     return dummy->next;
//     }
// };