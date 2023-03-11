class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head==None:
            return None
        if head.next==None:
            return TreeNode(head.val)
        slow,fast=head,head.next
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root