class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        a, b = 1, totalTrips * min(time)

        def f(x):
            return sum(x // t for t in time) >= totalTrips
    
        while a < b:
            m = (a + b) // 2
            if not f(m): a = m + 1
            else: b = m
        return a