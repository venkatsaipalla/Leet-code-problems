class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if mid > 0 and mid < n - 1:
                if nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    return nums[mid]
                elif (nums[mid] == nums[mid - 1] and mid % 2 == 1) or (nums[mid] == nums[mid + 1] and mid % 2 == 0):
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return 0
