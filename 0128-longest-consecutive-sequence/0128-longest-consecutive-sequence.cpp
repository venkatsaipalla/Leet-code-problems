class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n=nums.size();
        int longest=1;
        if(n==0) return 0;
        unordered_set<int>l;
        for(int i=0;i<n;i++){
            l.insert(nums[i]);
        }
        for(auto it: l){
            if(l.find(it-1)==l.end()){
                int count=1;
                int x=it;
                while(l.find(x+1)!=l.end()){
                    count++;
                    x=x+1;
                }
                longest=max(longest,count);
            }
        }
        return longest;
    }
};