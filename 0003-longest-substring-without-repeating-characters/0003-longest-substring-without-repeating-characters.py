class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        max_sub_len=1
        l=[]
        for i in s:
            if i in l:
                list_len=len(l)
                ind=l.index(i)
                if max_sub_len<list_len:
                    max_sub_len=list_len
                if ind+1==list_len:
                    l=[i]
                else:    
                    l=l[ind+1:]+[i]
            else:
                l.append(i)              
        return max(max_sub_len,len(l))        
                    
                    