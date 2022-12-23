class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product_so_far=nums[0]
        max_product_end=nums[0]
        min_product_end=nums[0]
        for i in range(1,len(nums)):
            temp=max(max(nums[i],nums[i]*max_product_end),nums[i]*min_product_end)
            min_product_end=min(min(nums[i],nums[i]*max_product_end),nums[i]*min_product_end)
            max_product_end=temp
            max_product_so_far=max(max_product_so_far,max_product_end)
        return max_product_so_far    