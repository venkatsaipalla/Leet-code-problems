class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
    #h