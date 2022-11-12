class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            else:
                i=i+2
                
        return nums[i]