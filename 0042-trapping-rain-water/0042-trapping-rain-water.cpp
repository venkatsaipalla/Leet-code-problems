class Solution {
public:
    int trap(vector<int>& height) {
            int n=height.size();
            vector<int>left(n,0);
            int lmax=height[0];
            left[0]=height[0];
            vector<int>right(n,0);
            int rmax=height[n-1];
            int count=0;
            for(int i=1;i<n;i++){
                lmax=max(lmax,height[i]);
                left[i]=lmax;
                rmax=max(rmax,height[n-i]);
                right[n-i]=rmax;
            }
            right[0]=max(rmax,height[0]);
            for(int i=0;i<n;i++){
                int temp=min(left[i],right[i])-height[i];
                count+=temp;
            }
        return count;
    }
};