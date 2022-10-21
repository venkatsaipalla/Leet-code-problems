class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x=[1,2,3]
        print(x[:5])
        if len(set(nums))==len(nums):
            return False
        for i in range(len(nums)):
            if len(set(nums[i:k+i+1]))<len(nums[i:k+i+1]):
                return True
        return False    