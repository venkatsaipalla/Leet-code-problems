class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=""
        for i in digits:
            x+=str(i)
        x=str(int(x)+1)
        y=list(map(int,list(x)))
        return y
        
        