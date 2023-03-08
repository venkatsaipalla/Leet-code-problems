class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            hours = 0
            
            for pile in piles:
                hours += ceil(pile / mid)
                
            if hours <= h:
                right = mid
            else:
                left = mid + 1
            
        return right