class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len=len(p)
        s_len=len(s)
        if p_len>s_len:
            return []
        pCount,sCount={},{}
        for i in range(p_len):
            pCount[p[i]]=1+pCount.get(p[i],0)
            sCount[s[i]]=1+sCount.get(s[i],0)
        
        res=[0] if sCount==pCount else []
        l=0
        
        for r in range(p_len,s_len):
            sCount[s[r]]=1+sCount.get(s[r],0)
            sCount[s[l]]-=1
            if sCount[s[l]]==0:
                sCount.pop(s[l])
            l+=1
            if sCount==pCount:
                res.append(l)
        return res        
            