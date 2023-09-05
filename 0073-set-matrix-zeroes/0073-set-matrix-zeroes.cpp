class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<vector<int>>temp;
        temp=matrix;
        int m=matrix.size();
        int n=matrix[0].size();
        cout<<m<<n<<endl;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(temp[i][j]==0){
                    int row=i;
                    int col=j;
                    while(row>=0){
                        matrix[row][j]=0;
                        row--;
                    }
                    row=i;
                    while(row<m){
                        matrix[row][j]=0;
                        row++;
                    }
                    while(col>=0){
                        matrix[i][col]=0;
                        col--;
                    }
                    col=j;
                    while(col<n){
                        matrix[i][col]=0;
                        col++;
                    }
                    
                }
            }
        }
        
    }
};