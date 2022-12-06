class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip(" ")
        l=s.split(" ")
        return len(l[-1])