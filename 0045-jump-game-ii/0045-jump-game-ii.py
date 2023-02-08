class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        
        reachableIndex = 0
        previousReachableIndex = 0
        jump = 0

        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]

            if curr == previousReachableIndex:
                jump += 1
                previousReachableIndex = reachableIndex
                if previousReachableIndex >= len(nums) - 1:
                    return jump
