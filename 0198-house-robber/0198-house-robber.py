class Solution:
    def rob(self, nums: List[int]) -> int:
        length=len(nums)
        if length == 1:
            return nums[0]
        
        if length == 2:
            return max(nums[0], nums[1])
        
        robFirst = nums[0]
        robSecond = max(nums[0], nums[1])
        
        for i in range(2, length):
            current = max(robSecond, robFirst + nums[i])
            
            robFirst = robSecond
            robSecond = current
            
        return robSecond