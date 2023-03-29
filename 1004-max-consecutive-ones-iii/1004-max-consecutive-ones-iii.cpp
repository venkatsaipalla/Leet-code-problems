class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n=nums.size();
        int ans=0;
        int flip=0;
        int i=0;
        int j=0;
        
        while(i<n){
            if(nums[i]==0){
                flip++;
            }
            
            while(flip>k){
                if(nums[j]==0)
                flip--;
                j++;
                    
            }
            
            ans=max(ans,i-j+1);
            i++;
        }
        
        return ans;
            
    }
};