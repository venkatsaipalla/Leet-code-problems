# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=0
        right=n
        mid=(left+right)//2
        while guess(mid)!=0:
            mid=(left+right)//2
            k=guess(mid)
            if k==0:
                return mid
            elif k<0:
                right=mid-1
            else:
                left=mid+1
        return mid