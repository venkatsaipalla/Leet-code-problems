class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        dup=0
        l=len(nums)
        tot=l*(l+1)//2
        s=sum(nums)
        for i in range(l):
            if nums[i] in d:
                dup=nums[i]
                break
            else:
                d[nums[i]]=1
        miss=tot-s+dup        
        return [dup,miss]
        