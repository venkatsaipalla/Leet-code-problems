class Solution:
    def frequencySort(self, s: str) -> str:
        x=dict(Counter(s))
        x=sorted(x.items(),key=lambda y:y[1],reverse=True)
        #ke=list(x.keys())
        #val=list(x.values())
        swaroop=""
        for i in x:
            swaroop+=i[0]*i[1]
        return swaroop