class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort() # sort trees according to x axis
        
        def cmpSlopes(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1) # if slope13 - slope12 > 0 => point 2 is under the line 13
        
        higher, lower  = [], []
        
        for point in trees:
            while len(higher) >= 2 and cmpSlopes(higher[-2], higher[-1], point) > 0: higher.pop() # pop point2 if slope12 < slope13
            while len(lower) >= 2 and cmpSlopes(lower[-2], lower[-1], point) < 0: lower.pop() # pop point2 if slope13 < slope12
            
            lower.append(tuple(point)) # append point 3 since last point in x-axis will always be part of boundary
            higher.append(tuple(point))   
        
        return set(lower + higher)