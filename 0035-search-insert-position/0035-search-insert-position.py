class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1]<target:
            return len(nums)
        elif target<=nums[0]:
            return 0
        else:            
            nums=nums+[target]
            nums.sort()
            start=0
            end=len(nums)-1
            res=0
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    res=mid
                    break
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            if nums[mid]==nums[mid-1]:
                return mid-1
            else:
                return mid
                