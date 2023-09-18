class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n=s.size();
        if(n==0) return 0;
        int maxCount=1;
        int count=1;
        map<char,int>map;
        map.insert({s[0],0});
        int i=1;
        int start=0;
        while(i<n){
           if(map.find(s[i])==map.end()){
               map[s[i]]=i;
               count++;
           }
            else if(map[s[i]]<start){
                map[s[i]]=i;
                    count++;
            }
           else{
               start=map[s[i]]+1;
               count=i-map[s[i]];
               map[s[i]]=i;
           } 
             maxCount=max(maxCount,count);
            i++;
        }
        return maxCount;
    }
};