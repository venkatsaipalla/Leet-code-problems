class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix[0].size();
        int n=matrix.size();
        int right=m*n-1;
        int left=0;
        while (left<=right){
            int mid=left+(right-left)/2;
            int row=mid/m;
            int col=mid%m;
            if(matrix[row][col]==target)
                return true;
            else if(matrix[row][col]<target){
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        return false; 
    }
};