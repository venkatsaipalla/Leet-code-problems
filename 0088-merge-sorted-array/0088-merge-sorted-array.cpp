class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1;
        int j=0;
        while( i>=0 and j<n){
            if(nums1[i]>nums2[j]){
                swap(nums1[i],nums2[j]);
                j++;
                i--;
            }
            else{
                break;
            }
        }
        sort(nums1.begin(),nums1.begin()+m);
        for(int k=0;k<nums1.size();k++){
            cout<<nums1[k];
        }
        sort(nums2.begin(),nums2.end());
        for(int j=0;j<n;j++){
            nums1[j+m]=nums2[j];
        }
        
    }
};