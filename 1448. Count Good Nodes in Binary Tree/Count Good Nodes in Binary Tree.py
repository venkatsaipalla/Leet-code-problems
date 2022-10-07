# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right =  right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:       
        count = 0
        def search(root, val):
            if not root:
                return
            if root.val>=val:
                nonlocal count
                count += 1
                val = root.val
            search(root.left,val)
            search(root.right,val)

        search(root,root.val)
        return count
