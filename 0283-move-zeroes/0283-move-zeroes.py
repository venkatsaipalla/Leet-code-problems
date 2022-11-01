class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[index] , nums[i] = nums[i],nums[index]
                index += 1 
        """
        count=0
        k=[]
        k[:]=nums
        for i in nums:
            print(i)
            if i==0:
                count=count+1
                k.remove(0)     
        l=[0]*count
        nums[:]=k+l
        """
            
        