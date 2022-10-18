class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return("1")
        x=self.countAndSay(n-1)
        i=0
        s=""
        while(i<len(x)):
            ch=x[i]
            ns=0
            while(i<len(x) and x[i]==ch):
                ns+=1
                i+=1
            s+=str(ns)
            s+=ch
        return(s)