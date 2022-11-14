class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        pos=0
        neg=1
        for i in nums:
            if i<0:
                res[neg]=i
                neg+=2
            else:
                res[pos]=i
                pos+=2
        return res        
                