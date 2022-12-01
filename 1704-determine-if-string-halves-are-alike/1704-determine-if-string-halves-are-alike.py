class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i=0
        j=len(s)-1
        volwes=['a','A','e','E','i','I','o','O','u','U']
        left=0
        right=0
        while i<j:
            if s[i] in volwes:
                left+=1
            if s[j] in volwes:
                right+=1
            i+=1
            j-=1
        return left==right    