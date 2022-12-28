class Solution:
      def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(0, len(piles)):
            piles[i] = -piles[i]

        heapq.heapify(piles)

        for i in range(0, k):
            heapq.heapreplace(piles, piles[0] // 2) # Trust me, I'm an engineer

        return -sum(piles)