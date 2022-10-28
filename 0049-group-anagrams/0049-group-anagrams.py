class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(strs)):
            l=list(strs[i])
            l.sort()
            l="".join(l)
            if l in d:
                d[l].append(i)
            else:
                d[l]=[i]
        
        print(d)
        indexs=list(d.values())
        print(indexs)
        res = []
        for i in indexs:
            l=[]
            for j in i:
                l.append(strs[j])
            res.append(l)    
        return res