class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n=nums.size();
        int major=nums[0];
        int count=1;
        for(int i=1;i<n;i++){
            if(count==0){
                major=nums[i];
                count++;
            }
            else if(nums[i]==major){
                count++;
            }
            else{
                count--;
            }
        }
        return major;
    }
};