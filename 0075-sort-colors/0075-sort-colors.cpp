class Solution {
public: 
    void swap(int &a,int &b){
            int temp=b;
            b=a;
            a=temp;
        }
        
    void sortColors(vector<int>& nums) {
       
        for(int i=0;i<nums.size();++i){
            for(int j=i+1;j<nums.size();++j){
                if(nums[i]>nums[j]){
                    swap(nums[i],nums[j]);
                }
            }
        }
    }
};