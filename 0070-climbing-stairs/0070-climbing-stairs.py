class Solution:
    d={1:1,2:2,3:3}
    def climbStairs(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        self.d[n]= self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.d[n]
        '''
        class Solution:
    d={1:1,2:2}
    def climbStairs(self, n: int) -> int:
        if self.d.get(n,0):return self.d.get(n)
        self.d[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.d[n]
        '''