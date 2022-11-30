class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        
        val=list(d.values())
        set_val=set(val)
        return len(val)==len(set_val)