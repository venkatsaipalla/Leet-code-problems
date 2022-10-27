class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
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
                
            
            