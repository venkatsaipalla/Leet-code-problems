# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l=[]
        def dfs(root):
            if root==None:
                return
            if root.left==None and root.right==None:
                l.append(root.val)
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root1)  
        l1=l.copy()
        l=[]
        dfs(root2)
        return l1==l