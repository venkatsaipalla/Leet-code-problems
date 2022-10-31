class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i-1][j-1]==matrix[i][j]:
                    continue
                else:
                    return False
        return True
        
        
        """
        row=len(matrix)
        col=len(matrix[0])
        i=0
        j=1
        while i<row:
            r=i
            c=0
            flag=0
            while r+1<row and c+1<col:
                if matrix[r][c]!=matrix[r+1][c+1]:
                    flag=1
                r=r+1
                c=c+1
            if flag==1:
                return False
            i=i+1
        while j<col:
            r=0
            c=j
            flag=0
            while r+1<row and c+1<col:
                if matrix[r][c]!=matrix[r+1][c+1]:
                    flag=1
                r=r+1
                c=c+1    
            if flag==1:
                return False 
            j=j+1
        return True    
        """
            
                
        
        
        