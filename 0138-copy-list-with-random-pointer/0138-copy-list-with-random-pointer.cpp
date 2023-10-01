/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head==NULL) return NULL;
        Node *dummy=head;
        map<Node*,Node*>map;
        while(dummy){
            Node *temp=new Node(dummy->val);
            map[dummy]=temp;
            dummy=dummy->next;
        }
        dummy=head;
        while(dummy){
            map[dummy]->next=map[dummy->next];
            map[dummy]->random=map[dummy->random];
            dummy=dummy->next;
        }
        return map[head];
    }
};