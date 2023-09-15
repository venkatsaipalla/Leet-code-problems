class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n=nums.size();
        if(n==0) return 0;
        unordered_set<int>st;
        for(int i=0;i<n;i++){
            st.insert(nums[i]);
        }
        int count=1;
        int longest=1;
        for(auto it : st){
            if(st.find(it-1)==st.end()){
                count=1;
                int x=it;
                while(st.find(x+1)!=st.end()){
                    count++;
                    x++;
                }
                longest=max(longest,count);
            }
            cout<<it<<endl;
        }
        return longest;
    }
};