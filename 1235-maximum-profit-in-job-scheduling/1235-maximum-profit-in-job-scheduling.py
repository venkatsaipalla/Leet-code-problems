class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))])
        heap = []
        
        max_profit_till_currStart, res = 0, 0                           
        for start, end, profit in jobs:     
            while heap and heap[0][0] <= start:
                _, tmp = heapq.heappop(heap)
                max_profit_till_currStart = max(max_profit_till_currStart, tmp)
            heapq.heappush(heap, (end, max_profit_till_currStart + profit))
            res = max(res, max_profit_till_currStart + profit)

        return res