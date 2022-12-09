# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        minimum=inf
        maximum=0
        def dfs(root,maximum,minimum):
            if root==None:
                return maximum-minimum
            maximum=max(maximum,root.val)
            minimum=min(minimum,root.val)
            return max(dfs(root.left,maximum,minimum),dfs(root.right,maximum,minimum))
        return dfs(root,maximum,minimum)

    