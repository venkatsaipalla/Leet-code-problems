class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        l1 = {c:i for i,c in enumerate(order)}
        l2 = [[l1[i] for i in word] for word in words]
        return l2 == sorted(l2)