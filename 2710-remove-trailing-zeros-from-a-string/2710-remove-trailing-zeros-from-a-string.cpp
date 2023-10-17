class Solution {
public:
    string removeTrailingZeros(string num) {
        string res="";
        int i=0;
        int n=num.size();
        while(i<n){
            if(num[i]=='0'){
                string temp="";
                while(i<n and num[i]=='0'){
                    temp+=num[i];
                    i++;
                }
                if(i<n){
                    res+=temp;
                }
            }
            else{
                res+=num[i];
                i++;
            }
        }
        return res;
    }
};