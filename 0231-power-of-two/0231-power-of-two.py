class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        if n<=0:
            return False
        return (math.log10(n)/math.log10(2))%1==0