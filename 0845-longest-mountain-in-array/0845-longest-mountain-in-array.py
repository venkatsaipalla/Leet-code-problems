class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_len=0
        n=len(arr)
        i=1
        while i<=n-2:
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                count=1
                j=i
                while j>0 and arr[j]>arr[j-1]:
                    j-=1 
                    count+=1 
                while i<n-1 and arr[i]>arr[i+1]:
                    i+=1 
                    count+=1 
                max_len=max(max_len,count)    
            else:
                i+=1 
        return(max_len)    