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
#include <iostream>
using namespace std;
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode* start= new ListNode(0);
        start=head;
        vector<int>arr={};
        int i,j,key,n;
        while(start!=NULL){
            arr.push_back(start->val);
            start=start->next;
        }
        n=arr.size();
        for(i=1;i<n;i++){
            key=arr[i];
            j=i-1;
            while(j>=0 && arr[j]>key){
                arr[j+1]=arr[j];
                j--;
            }
            arr[j+1]=key;      
        }
        ListNode* dummy = new ListNode(0);
        dummy->val=arr[0];
        head=dummy;
        for(i=1;i<n;i++){
            ListNode* temp = new ListNode(arr[i]);
            dummy->next=temp;
            dummy=dummy->next;
        }
        return head;
    }
};