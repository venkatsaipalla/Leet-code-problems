class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int s=nums.size();
        int pos=0;
        int neg=1;
        vector<int>res(s,0);
            for(int i=0;i<s;i++){
                if(nums[i]<0){
                    res[neg]=nums[i];
                    neg=neg+2;
                }
                else{
                    res[pos]=nums[i];
                        pos=pos+2;
                }
            }
        return res;
    }
};