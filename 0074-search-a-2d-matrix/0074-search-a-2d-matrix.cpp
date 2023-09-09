class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int i=matrix.size()-1;
        int j=0;
        int n=matrix[0].size();
        // cout<<i<<n;
        while(i>=0 and j<n){
            cout<<i<<" "<<j<<endl;
            if(matrix[i][j]==target){
                return true;
            }
            else{
                if(matrix[i][j]<target){
                j++;
            }
            else{
                i--;
            }
            }
        }
        return false; 
    }
};