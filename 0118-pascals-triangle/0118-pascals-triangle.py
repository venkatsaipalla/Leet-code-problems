class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        l=[[1],[1,1]]
        i=1
        while i<numRows-1:
            x=l[-1]
            temp=[x[0]]
            j=0
            while j+1<len(x):
                temp.append(x[j]+x[j+1])
                j=j+1
            temp.append(x[-1])
            l.append(temp)
            i=i+1
        return l    
            
        