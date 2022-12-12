class Solution:
    d={1:1,2:2,3:3}
    def climbStairs(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        self.d[n]= self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.d[n]
