class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)//2
        stack=[]
        openn=["(","{","["]
        mapp={
            ")":"(",
              "}":"{",
              "]":"["
             }
        for i in s:
            if i in openn:
                stack.append(i)
            elif stack!=[]:
                temp=stack.pop()
                if temp!=mapp[i]:
                    return False
            else:
                return False
        if stack==[]:
            return True 
        else:
            return False