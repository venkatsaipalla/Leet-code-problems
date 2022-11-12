class Solution:
    def rob(self, nums: List[int]) -> int:
        length=len(nums)
        if length==1:
            return nums[0]
        if length==2:
            return max(nums[0],nums[1])
        else:
            nums[1]=max(nums[1],nums[0])
            for i in range(2,len(nums)):
                nums[i]=max(nums[i]+nums[i-2],nums[i-1])
            return nums[-1]    