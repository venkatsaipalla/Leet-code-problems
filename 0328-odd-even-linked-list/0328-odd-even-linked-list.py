# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        result=head
        if head==None or head.next==None:
            return head
        else:
            even=head
            odd=head.next
            even_list=[]
            odd_list=[]
            while odd and odd.next:
                even_list.append(even.val)
                even=even.next.next
                odd_list.append(odd.val)
                odd=odd.next.next
            if even:
                even_list.append(even.val)
            if odd:
                odd_list.append(odd.val)
            res=even_list+odd_list  
            print(res)
            i=0
            while start:
                start.val=res[i]
                start=start.next
                i+=1
            return result
            
            
            
        