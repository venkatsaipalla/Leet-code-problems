class Solution:
    def removeElement(self, nums, val):
        i = 0
        #loop
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i