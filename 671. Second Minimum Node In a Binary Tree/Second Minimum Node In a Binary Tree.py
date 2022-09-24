# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        a=[]
        def call(root: Optional[TreeNode]):
            if root==None:
                return
            call(root.left)
            a.append(root.val)
            call(root.right)
        
        call(root)
        print(a)
        k=set(a)
        k=list(k)
        if len(k)<2:
            return -1
        k.sort()
        return k[1]
