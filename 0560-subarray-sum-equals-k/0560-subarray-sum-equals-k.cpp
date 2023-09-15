class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n=nums.size();
        int count=0;
        long long prefixSum=0;
        map<int,int>temp;
        temp[0]=1;
        //Optimal Approach
        for(int i=0;i<n;i++){
            prefixSum+=nums[i];
            int remove=prefixSum-k;
            count+=temp[remove];
            temp[prefixSum]+=1;
        }
        
        
        //Better Approach
        // long long sum=0;
        // for(int i=0;i<n;i++){
        //     sum=0;
        //     for(int j=i;j<n;j++){
        //         sum+=nums[j];
        //         if(sum==k){
        //             count++;
        //         }
        //     }
        // }
        return count;
    }
};