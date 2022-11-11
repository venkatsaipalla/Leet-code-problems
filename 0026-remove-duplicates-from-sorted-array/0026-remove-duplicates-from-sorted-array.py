class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x= list(set(nums))
        x.sort()
        x_len=len(x)
        l=['_']*(len(nums)-x_len)
        nums[::]=x+l
        return x_len
            