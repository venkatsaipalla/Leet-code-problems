class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        dup=0
        length=len(nums)
        l=list(range(1,length+1))
        tot=sum(l)
        s=sum(nums)
        for i in range(length):
            if nums[i] in d:
                dup=nums[i]
                break
            else:
                d[nums[i]]=1
        miss=tot-s+dup        
        return [dup,miss]
        