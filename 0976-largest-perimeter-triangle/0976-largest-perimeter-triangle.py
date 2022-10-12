class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        length=len(nums)
        if length<3:
            return 0
        nums.sort(reverse=True)
        for i in range(length-2):
            if nums[i+2]+nums[i+1]>nums[i]:
                return nums[i]+nums[i+1]+nums[i+2]
        print(nums)
        
        return 0