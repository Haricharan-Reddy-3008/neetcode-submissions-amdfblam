class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans=set()

        for num in nums:
            if num in ans:
                return True
            ans.add(num)  

        return False

obj = Solution()
result = obj.hasDuplicate([1,2,3,3])
print(result)


        