class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans^=i
        return ans
        
        """
        nums.sort()
        print(nums)
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            else:
                i=i+2
                
        return nums[i]
        """