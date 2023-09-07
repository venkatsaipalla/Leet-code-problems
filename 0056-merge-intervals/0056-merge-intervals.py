class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        i=0
        n=len(intervals)
        intervals.sort()
        for i in range(n):
            start=intervals[i][0]
            end=intervals[i][1]
            if len(res)>0 and res[-1][1]>=end:
                continue;
            for j in range(i+1,n):
                if intervals[j][0]<=end:
                    end=max(intervals[j][1],end)
                else:
                    break
            res.append([start,end])
        return res    
                