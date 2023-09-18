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
        cout<<"-----------"<<endl;
        int start=0;
        while(i<n){
            
           if(map.find(s[i])==map.end()){
               map[s[i]]=i;
               cout<<"map--i="<<i<<"  "<<map[s[i]]<<endl;
               count++;
           }
            else if(map[s[i]]<start){
                map[s[i]]=i;
                    count++;
            }
           else{
               start=map[s[i]]+1;
               count=i-map[s[i]];
               // for(auto itr:map){
               //     if(itr.second<map[s[i]]) map.erase(itr.first);
               // }
               //  for(auto itr:map){
               //     cout<<itr.first;
               // }
               cout<<endl;
               cout<<"duplicate s[i] = "<<s[i]<<" map->"<<map[s[i]]<<endl;
               map[s[i]]=i;
           } 
             maxCount=max(maxCount,count);
            cout<<"\ni = "<<i<<" s[i] = "<<s[i]<<"  "<<"count = "<<count<<endl;
            i++;
        }
        return maxCount;
    }
};