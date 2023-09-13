class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n=nums.size();
        map<int,int>map;
        for(int i=0;i<n;i++){
            int more=target-nums[i];
            if(map.find(more)!=map.end()){
                return {map[more],i};
            }
            map[nums[i]]=i;
        }
        return {-1,-1};
    }
};