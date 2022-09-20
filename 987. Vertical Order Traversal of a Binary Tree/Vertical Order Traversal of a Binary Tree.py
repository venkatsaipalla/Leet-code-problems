# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        Q = deque()
        dic = {}
        dic[0] = [(0, root.val)]
        Q.append( (root, 0, 0) )
        while Q:
            node, col, row = Q.popleft()
            if node.left:
                dic[col - 1] = dic.get(col - 1, [])
                dic[col - 1].append( (row + 1, node.left.val) )
                Q.append( (node.left, col - 1, row  + 1) )
            if node.right:
                dic[col + 1] = dic.get(col + 1, [])
                dic[col + 1].append( (row + 1, node.right.val) )
                Q.append( (node.right, col + 1, row  + 1) )
        
        res = []
        for _, RowVal in sorted(dic.items()):
            t = []
            for item in sorted(RowVal):
                t.append(item[1])
            res.append(t)
            
        return res
