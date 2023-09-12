class Solution {
public:
    int countPaths(int i,int j,int m,int n,vector<vector<int>>&dp){
         if(i==m-1 and j==n-1) return 1;
        if(i>=m or j>=n) return 0;
        if(dp[i][j]!=-1) return dp[i][j];
        else return dp[i][j]=countPaths(i+1,j,m,n,dp)+countPaths(i,j+1,m,n,dp);
    }
    
    int uniquePaths(int m, int n) {
       vector<vector<int>>dp(m,vector<int>(n,-1));
        return countPaths(0,0,m,n,dp);
    }
};