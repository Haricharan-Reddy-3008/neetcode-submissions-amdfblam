class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ=0
        l=0
        result=float('inf')

        for r in range(len(nums)):

            summ+=nums[r]

            while summ >=target:
                result=min(result,r-l+1)
                summ-=nums[l]
                l+=1
        if result == float('inf'):

            return 0

        return result

            
                
        
        