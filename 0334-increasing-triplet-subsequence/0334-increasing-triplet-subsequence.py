class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left =inf
        right=inf
        for i in nums:
            if i>right:
                return True
            elif i>left and i<right:
                right=i
            elif i<left:
                left=i
            print(left,right)    
        return False        
        