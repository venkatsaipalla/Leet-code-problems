class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n==len(nums):
            return nums
        l=nums[:-n]
        r=nums[-n::1]
        print(l)
        print(r)
        arr=[]
        for i in range(n):
            arr.append(l[i])
            arr.append(r[i])
        arr+=nums[2*n:]
        return arr