# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        def depthLeft(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def depthRight(node):
            d = 0
            while node:
                d += 1
                node = node.right
            return d
        
        ld = depthLeft(root.left)
        rd = depthRight(root.right)
        
        if ld == rd:
            return 2**(ld + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        