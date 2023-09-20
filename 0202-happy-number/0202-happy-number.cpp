class Solution {
public:
    int calSquareSum(int n){
        int sum=0;
        while(n>0){
            int digit=n%10;
            sum+=pow(digit,2);
            n=n/10;
        }
        return sum;
    }
    bool isHappy(int n) {
        bool ans=false;
        map<int,int>map;
        while(true){
            int temp=calSquareSum(n);
            if(map.find(temp)==map.end()){
                map[temp]++;
            }
            else{
                break;
            }
            n=temp;
            if(temp==1){
                ans=true;
                break;
            }
        }
        return ans;
    }
};