class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int n=nums.size();
        vector<vector<int>>ans;
        sort(nums.begin(),nums.end());
        for(int p=0;p<n;p++){
            if(p>0 and nums[p]==nums[p-1]) continue;
            int x=target-nums[p];
        for(int i=p+1;i<n;i++){
            if(i>p+1 and nums[i]==nums[i-1]) continue;
            int j=i+1;
            int k=n-1;
            while(j<k){
                long long sum = nums[i];
                sum+=nums[j];
                sum+=nums[k];
                if(sum<x){
                    j++;
                }
                else if(sum>x){
                    k--;
                }
                else{  
                    vector<int>temp={nums[p],nums[i],nums[j],nums[k]};
                    ans.push_back(temp);
                    j++;
                    k--;
                    while(j<k and nums[j]==nums[j-1]) j++;
                    while(j<k and nums[k]==nums[k+1]) k--;
                }
            }
        }
         }    
        return ans;
    }
};