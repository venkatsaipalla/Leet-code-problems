# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        start=1
        end=n
        while start<end:
            mid=(start+end)//2
            if isBadVersion(mid):
                end=mid
            else:
                start=mid+1
        return start        
                
        """
        if n==1:
            return 1
        nums=list(range(1,n+1))
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            check_mid=isBadVersion(nums[mid])
            if check_mid:
                end=mid-1
                if isBadVersion(nums[end])==False:
                    return mid
            else:
                start=mid+1
                if isBadVersion(nums[start]):
                    return start
        """        