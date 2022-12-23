class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        def peak_arr(arr,low,high):
            if low>=high:
                return low
            mid= (low+high)//2
            if arr[mid]<arr[mid+1]:
                return  peak_arr(arr,mid+1,high)
            else:
                return peak_arr(arr,low,mid)
            return peak_arr(arr,0,len(arr)) 
        return peak_arr(arr,0,len(arr))   
     