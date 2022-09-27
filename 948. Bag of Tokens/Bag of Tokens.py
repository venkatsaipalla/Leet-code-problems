class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i=0
        j=len(tokens)-1
        score=0
        max_score=0
        while i<=j:
            if tokens[i]<=power:
                power-=tokens[i]
                score+=1
                i+=1
                if max_score<score:
                    max_score=score
            elif score>0:
                power+=tokens[j]
                score-=1
                j-=1
            else:
                return max_score
        return max_score        
                    
