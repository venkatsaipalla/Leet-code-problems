class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l=len(palindrome)
        x=list(palindrome)
        print(x)
        flag=0
        if l==1:
            return ""
        for i in range(l):
            if x[i]!='a':
                c=x[i]
                x[i]='a'
                if x!=x[::-1]:
                    return "".join(x)
                x[i]=c
        if flag==0:
            x[-1]='b'
            return "".join(x)
            
                    
        
        
        