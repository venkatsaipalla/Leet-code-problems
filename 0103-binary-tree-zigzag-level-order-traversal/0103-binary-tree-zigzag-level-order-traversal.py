# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        ans = []
        self.addLevel(ans, 0, root)#level from 0
        return ans
        
        
    def addLevel(self, ans, level, root):
        if not root:
            return
        elif len(ans) <= level:
                ans.append([root.val])
        elif not level%2:#if it is an even level, then then level ans should be inversed, so I use extend founction
            ans[level].extend([root.val])
        else:
            ans[level].insert(0,root.val)# if it is an odd level, then level ans should be ordinal, so I use insert function
        self.addLevel(ans, level + 1, root.left)
        self.addLevel(ans, level + 1, root.right)