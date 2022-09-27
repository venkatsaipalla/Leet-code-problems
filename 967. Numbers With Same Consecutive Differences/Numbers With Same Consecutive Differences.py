class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n==1:
            return range(10)
        q=range(1, 10)
        for i in range(n-1):
            tmp=[]
            for i in q:
                for d in set([i%10+k, i%10-k]):
                    if 0<=d<10:
                        tmp.append(i*10+d)
            q=tmp
        return q
