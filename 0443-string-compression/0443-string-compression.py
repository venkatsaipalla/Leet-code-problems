class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        start=chars[0]
        count=0
        l=len(chars)
        if l==1:
            return 1
        for i in range(l):
            if start==chars[i]:
                count+=1
            else:
                if count==1:
                    s+=start
                else:
                    s+=start+str(count)
                start=chars[i]
                count=1
            
            if i==l-1:
                if count==1:
                    s+=start
                else:
                    s+=start+str(count)
        chars[:]=s
        return len(s)
        