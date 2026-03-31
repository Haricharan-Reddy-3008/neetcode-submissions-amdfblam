class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        seen={}
        for i,num in enumerate (nums):
            complement=target-num

            if complement in seen:
                return [seen[complement],i]

            seen[num]=i    

obj = Solution()
result = obj.twoSum([2, 7, 11, 15], 9)
print(result)
            



        