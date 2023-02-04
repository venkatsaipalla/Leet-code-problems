class Solution:
    def checkInclusion(self, s1, s2):
        if not s1: return True
        letters = collections.Counter(s1)
        lCnt, j = len(s1), 0
        for i in range(len(s2)):
            if s2[i] not in letters or letters[s2[i]] == 0 : # DNE or depleted
                while j < i and s2[j] != s2[i]: 
                    letters[s2[j]] += 1; j += 1
                if s2[j] in letters: letters[s2[j]] += 1 # if in char map
                j += 1 
            elif i-j+1 == lCnt: return True
            if s2[i] in letters: letters[s2[i]] -= 1
        return False
