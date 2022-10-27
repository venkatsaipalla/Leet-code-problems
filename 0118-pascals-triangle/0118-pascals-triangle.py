class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        while len(l)<numRows:
            x=l[-1]
            temp=[1]
            j=0
            while j+1<len(x):
                temp.append(x[j]+x[j+1])
                j=j+1
            temp.append(1)
            l.append(temp)
        return l    
            
        