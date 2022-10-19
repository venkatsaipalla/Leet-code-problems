class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        words=sorted(words)
        x=Counter(words)
        y=sorted(x.items(),key=lambda z:z[1],reverse=True)
        p=[i[0] for i in y]
        return p[:k]
        