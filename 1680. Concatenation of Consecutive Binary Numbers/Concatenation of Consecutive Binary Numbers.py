*method 1*
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9 +7
        size=0
        res=0
        for i in range(1,n+1):
            if(i&(i-1)==0):
                size+=1
            res=((res<<size)%mod +i)%mod
        return res 
      
*method 2*
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res=""
        for i in range(1,n+1):
            res+=bin(i).replace('0b','')
        return int(res,2) %(10**9 +7)
