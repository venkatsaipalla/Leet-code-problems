class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0                                     # Ex: plantTime = [1,2,3,2]
                                                    #      growTime = [2,1,2,1]

        for g,p in sorted(zip(growTime,plantTime)): #   p    g   ans
            ans = g + p if g >= ans else ans + p    #  –––  –––  ––––
                                                    #   1    2    3
        return ans