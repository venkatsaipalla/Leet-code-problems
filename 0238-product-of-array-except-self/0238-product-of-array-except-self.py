class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct=1
        zeroCount=0
        totalNonZeroProduct=1
        for i in nums:
            if i==0:
                zeroCount+=1
                totalProduct=0
            else:
                totalProduct*=i
                totalNonZeroProduct*=i
        lenght=len(nums)        
        answer=[1]*lenght
        if zeroCount>1:
            return [0]*lenght
        for i in range(lenght):
            if nums[i]==0:
                answer[i]=totalNonZeroProduct
            else:
                answer[i]=totalProduct//nums[i]
        return answer        
            
        