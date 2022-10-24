class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = [set(s) for s in arr if len(s) == len(set(s))] # obviate duplicates

        def dfs(chars, i):
            if i == len(charSet):
                return len(chars)
            if not chars.intersection(charSet[i]): # disjoint
                return max(dfs(chars.union(charSet[i]), i + 1), # choose set[i]
                           dfs(chars, i + 1)) # not choose set[i]
            else:
                return dfs(chars, i + 1)
            
        return dfs(set(), 0)