class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1=dict(Counter(nums1))
        d1_keys=list(d1)
        d1_values=d1.values()
        
        d2=dict(Counter(nums2))
        d2_keys=list(d2)
        d2_values=d2.values()
  
        res=[]
        if len(d1_keys)>len(d2_keys):
            for i in d1_keys:
                if i in d2_keys:
                    res+=[i]*min(d1[i],d2[i])
        else:
            for i in d2_keys:
                if i in d1_keys:
                    res+=[i]*min(d1[i],d2[i])
        return res