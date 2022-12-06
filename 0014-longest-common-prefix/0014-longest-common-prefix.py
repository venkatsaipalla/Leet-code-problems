class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        j=0
        length=len(strs)
        while j<len(strs[0]):
            res=strs[0][:j+1:]
            for i in range(1,length):
                if res != strs[i][:j+1:]:
                    return res[:-1:]
            j+=1    
        return res        
            