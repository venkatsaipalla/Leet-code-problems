class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l=len(isConnected)
        rank=[1]*l
        par=[i for i in range(l)]
        
        def find(n1):
            res=n1
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2]=p1
                rank[p1]+=p2
            return 1
        res=l
        for i in range(l):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    res-=union(i,j)
                    
        return res            