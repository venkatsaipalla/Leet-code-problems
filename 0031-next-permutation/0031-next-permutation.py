class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use two-pointers: two pointers start from back
        # first pointer j stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        if not nums: return None
        i = len(nums)-1
        j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step
        while i > 0:
            if nums[i-1] < nums[i]: # first one violates the trend
                j = i-1
                break
            i-=1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]: # 
                nums[i], nums[j] = nums[j], nums[i] # swap position
                nums[j+1:] = sorted(nums[j+1:]) # sort rest
                return
        """all_perm=[]
        def permutations (x):
            if len(x)==0:
                return []
            elif len(x)==1:
                return [x]
            else:
                temp=[]
                for i in range(len(x)):
                    fixed=x[i]
                    remaing=x[:i]+x[i+1:]
                    for p in permutations(remaing):
                        temp.append([fixed]+p)
                return temp      
        for i in permutations(nums):
            all_perm.append(i)
        all_perm.sort()
        print(all_perm)
        index_value=all_perm.index(nums)
        if index_value==len(all_perm)-1:
            nums=all_perm[0]
        else:
            nums=all_perm[index_value+1]"""
            