class Solution {
public: 
    void swap(int &a,int &b){
            int temp=b;
            b=a;
            a=temp;
        }
        
    void sortColors(vector<int>& nums) {
       
        for(int i=1;i<nums.size();++i){
            int j=i-1;
            int key=nums[i];
            while(j>=0 and nums[j]>key){
                nums[j+1]=nums[j];
                j--;
            }
            nums[j+1]=key;
        }
    }
};