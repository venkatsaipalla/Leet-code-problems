class Solution:
    def countGoodNumbers(self, n: int) -> int:
        res = 1
        a, b = (n+1)//2, n//2
        MOD = 10**9 + 7
        return pow(5,a,MOD)*pow(4,b,MOD)%MOD