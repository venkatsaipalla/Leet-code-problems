class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int len=nums.size();
        // int[] l= new int[len+1];
    vector<int> l(len);
        for(int i=0;i<len;++i){
           l[nums[i]]++;
            if(l[nums[i]]>1){
                return nums[i];
            }
        }
        return len;
    }
};