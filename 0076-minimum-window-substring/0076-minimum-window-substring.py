class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        h = collections.Counter(t)
        cnt = len(h)
        n = len(s)
        mini = n+1
        start, end = 0, -1
        lo = 0
        
        for hi in range(n):
            if(s[hi] in h):
                h[s[hi]] -= 1
                cnt -= h[s[hi]] == 0
            while(not cnt):
                if(hi-lo+1 < mini):
                    mini = hi-lo+1
                    start, end = lo, hi
                if(s[lo] in h):
                    h[s[lo]] += 1
                    cnt += h[s[lo]] == 1
                lo += 1
                
        return s[start:end+1]