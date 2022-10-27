class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Medthod 1
        """
        row=len(matrix)
        col=len(matrix[0])
        d=[]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    d.append([i,j])
        for i in d:
            for r in range(row):
                matrix[r][i[1]]=0
            for c in range(col):
                matrix[i[0]][c]=0
                
        """
        #Method 2
        row=len(matrix)
        col=len(matrix[0])
        r=set()
        c=set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        
        for i in r:
            for j in range(col):
                matrix[i][j]=0
        for i in range(row):
            for j in c:
                matrix[i][j]=0
                
            
            