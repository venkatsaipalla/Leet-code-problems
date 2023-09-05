class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        leng=len(nums)
        arr=[0]*leng
        for i in nums:
            arr[i]+=1
            if(arr[i]>1):
                return i
            