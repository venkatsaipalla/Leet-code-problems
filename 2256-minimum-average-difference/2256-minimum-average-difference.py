class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l=[0,inf]
        n=len(nums)
        if n==1:
            return 0
        
        """def rd(i):
            if isinstance(i, float):
                if (abs(i)%1)*10>5:
                    return int (i) + 1
                else:
                    return int (i)
            else: return i"""
        right_sum = sum(nums)
        left_sum=0
        for i in range(0,n):
            if i==n-1:
                right=0
            else:
                right_sum=right_sum-nums[i]
                right=right_sum//(n-i-1)
            left_sum+=nums[i]    
            left=left_sum//(i+1)
            temp=abs(left-right)
            #print("index",i,"  ","left",left,"right",right,"temp ",temp)
            if l[1]>temp:
                l[0]=i
                l[1]=temp
        return l[0]        