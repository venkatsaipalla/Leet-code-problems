class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr=s.split(" ")
        d1={}
        d2={}
        for j in range(len(pattern)):
            if pattern[j] not in d1:
                d1[pattern[j]]=[j]
            else:
                d1[pattern[j]].append(j)
        for i in range(len(arr)):
            if arr[i] not in d2:
                d2[arr[i]]=[i]
            else:
                d2[arr[i]].append(i)
        return list(d1.values())==list(d2.values())       
