//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
/*You are required to complete this function*/

class Solution{
    public:
    int maxLen(vector<int>&A, int n)
    {   
        // Your code here
        int maxLen=0;
        map<int,int>prefixmap;
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=A[i];
            if(sum==0){
                maxLen=max(maxLen,i+1);
            }
            int rem=sum;
            if(prefixmap.find(rem)!=prefixmap.end()){
                int le=i-prefixmap[rem];
                maxLen=max(le,maxLen);
            }
            if(prefixmap.find(sum)==prefixmap.end())
            {
                prefixmap[sum]=i;
                
            };
        }
        
        return maxLen;
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int m;
        cin>>m;
        vector<int> array1(m);
        for (int i = 0; i < m; ++i){
            cin>>array1[i];
        }
        Solution ob;
        cout<<ob.maxLen(array1,m)<<endl;
    }
    return 0; 
}



// } Driver Code Ends