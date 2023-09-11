class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        ans=nums[0]
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
                if d[i]>n/2:
                    ans=i
                    break
            else:
                d[i]=1
        return ans