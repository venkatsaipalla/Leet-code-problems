class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0 
        stack = []
        for i in range(len(arr)+1): 
            while stack and (i == len(arr) or arr[stack[-1]] > arr[i]): 
                mid = stack.pop()
                ii = stack[-1] if stack else -1 
                ans += arr[mid] * (i - mid) * (mid - ii)
            stack.append(i)
        return ans % 1_000_000_007