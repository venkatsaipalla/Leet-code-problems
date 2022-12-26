class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j=0
        for i in range(len(nums)):
            if i>j:
                return False
            j=max(j,i+nums[i])
        return True   