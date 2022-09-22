class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        l=list(map(lambda x:x[::-1],l))
        x=" ".join(l)
        return x
