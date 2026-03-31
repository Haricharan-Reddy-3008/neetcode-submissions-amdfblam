class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd=1
        zerocnt=0

        for num in nums:
            if num:
                prd=prd*num
            else:
                zerocnt+=1  
        if zerocnt>1 : return [0]*len(nums) 

        res=[0]*len(nums)
        for i,c in enumerate(nums):
            if zerocnt:res[i]=0 if c else prd
            else:res[i]=prd//c

        return res




