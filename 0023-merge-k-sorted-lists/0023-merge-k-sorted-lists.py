class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s=[]
        head=n=ListNode(0)
        for i in range(len(lists)):
            while lists[i]!=None:
                s.append(lists[i].val)
                lists[i]=lists[i].next
        s.sort()
        for i in range(len(s)):
            n.next=ListNode(s[i])
            n=n.next
        return head.next