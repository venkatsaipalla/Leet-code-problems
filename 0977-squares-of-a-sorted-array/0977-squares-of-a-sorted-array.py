class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        j=len(nums)-1
        k=j
        i=0
        while(i<=j):
            s=nums[i]*nums[i]
            t=nums[j]*nums[j]
            if s<t:
                ans[k]=t
                j-=1
            else:
                ans[k]=s
                i+=1
            k-=1
        return ans