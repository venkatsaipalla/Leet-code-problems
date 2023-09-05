class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left=0;
        int len=nums.size()-1;
        int right=len;
        vector<int>temp;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(nums[mid]<target){
                left=mid+1;
            }
            else if(nums[mid]>target){
                right=mid-1;             
            }
            else{
                left=mid;
                right=mid;
                while(left>=0 and nums[left]==target){
                    left--;
                }
                while(right<=len and nums[right]==target){
                    right++;
                }
                temp.push_back(left+1);
                temp.push_back(right-1);
                return temp;
            }
        }
        temp.push_back(-1);
        temp.push_back(-1);
        return temp;
    }
};