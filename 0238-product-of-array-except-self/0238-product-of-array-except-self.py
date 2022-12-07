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
        answer=[]
        if zeroCount>1:
            return [0]*len(nums)
        for i in nums:
            if i==0:
                answer.append(totalNonZeroProduct)
            else:
                answer.append(totalProduct//i)
        return answer        
            
        