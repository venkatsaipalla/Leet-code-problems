class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        x,a,b = -1,-2,-2
        res = 0
        for i,n in enumerate(nums):
            if n>maxK or n<minK: x = i
            if n == minK: a = i
            if n == maxK: b = i
            res += max(0, min(a,b) - x)
        return res