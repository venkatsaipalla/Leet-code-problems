class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n=nums.size();
        int cnt1=0;
        int el1=INT_MIN;
        int cnt2=0;
        int el2=INT_MIN;
        for(int i=0;i<n;i++){
            if(cnt1==0 and nums[i]!=el2){
                cnt1=1;
                el1=nums[i];
            }
            else if(cnt2==0 and nums[i]!=el1){
                cnt2=1;
                el2=nums[i];
            }
            else if(nums[i]==el1){
                cnt1++;
            }
            else if(nums[i]==el2){
                cnt2++;
            }
            else{
                cnt1--;
                cnt2--;
            }
        }
        cnt1=0;
        cnt2=0;
        for(int i=0;i<n;i++){
            if(nums[i]==el1) cnt1++;
            if(nums[i]==el2) cnt2++;
        }
        int min=n/3;
        vector<int>temp;
        cout<<cnt1<<" "<<cnt2<<endl;
        if(cnt1>min) temp.push_back(el1);
        if(cnt2>min) temp.push_back(el2);
        return temp;
     }};