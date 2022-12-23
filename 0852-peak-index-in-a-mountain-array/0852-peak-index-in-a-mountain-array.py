class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        def peak_arr(arr,left,right):
            mid= (left+right)//2
            print(mid)
            if arr[mid-1]<=arr[mid]>=arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid] and mid>0:
                return  peak_arr(arr,left,mid-1)
            else:
                return peak_arr(arr,mid+1,right)
        return peak_arr(arr,0,len(arr))   