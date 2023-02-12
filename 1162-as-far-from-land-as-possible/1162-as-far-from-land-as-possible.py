class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        queue=[]
        visited=set()
        for x,y in itertools.product(range(n),range(n)):
            if grid[x][y]:
                visited.add((x,y))
                queue.append([x,y,0])
        final=0
        while queue:
            x1,y1,cnt=queue.pop(0)
            final=max(final,cnt)
            for x2,y2 in {(x1+1,y1),(x1-1,y1),(x1,y1+1),(x1,y1-1)}:
                if 0<=x2<n and 0<=y2<n and (x2,y2) not in visited:
                    visited.add((x2,y2))
                    queue.append([x2,y2,cnt+1])
            
        return final if final else -1