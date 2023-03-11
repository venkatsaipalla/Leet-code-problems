# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.ran=[]
        while head:
            self.ran.append(head.val)
            head=head.next
    def getRandom(self) -> int:
        i=int(random.random()*len(self.ran))            
        return self.ran[i]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()