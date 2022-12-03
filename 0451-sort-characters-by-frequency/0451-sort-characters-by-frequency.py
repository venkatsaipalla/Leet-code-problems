class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        l = sorted(list(set(s)), key=s.count, reverse=True)
        for i in l:
            ans += i * s.count(i)
        return ans