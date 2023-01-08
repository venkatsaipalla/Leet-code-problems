class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                if max_count<count:
                    max_count=count
                count=0
        if max_count<count:
            max_count=count
        return max_count        