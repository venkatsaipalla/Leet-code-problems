class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size();
        cout<<left<<right<<endl;
        if(nums[right-1]>=target){
        while(left<=right){
            int mid= left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]<target){
                left=mid+1;
            }
            else if(nums[mid]>target){
                right=mid-1;
            }
        }
        cout<<"outside";
        return right+1;
        }
        else if(target<=nums[0]){
            return 0;
        }
        else{
return right;}
    }
};