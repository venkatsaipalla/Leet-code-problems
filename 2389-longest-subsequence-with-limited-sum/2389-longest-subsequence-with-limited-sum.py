class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()  # O(n log n) time, O(n/2) space
        # Create prefix sum. No need for extra space. Reuse nums[]
        for i in range(1, len(nums)):  # O(n)
            nums[i] += nums[i-1]
        # No need for extra space for answer. Resuse queries[]
        for i in range(len(queries)):  # n times
            queries[i] = bisect.bisect_right(nums, queries[i]) # O(log n)
        return queries