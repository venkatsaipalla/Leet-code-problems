class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        k=[]
        k[:]=nums
        for i in nums:
            print(i)
            if i==0:
                count=count+1
                k.remove(0)
        print("k =",k,"Count = ",count)        
        l=[0]*count
        nums[:]=k+l
            
        