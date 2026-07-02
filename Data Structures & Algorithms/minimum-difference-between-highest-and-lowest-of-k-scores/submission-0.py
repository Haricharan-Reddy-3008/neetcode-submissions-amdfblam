class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        window=nums[:k]
        res = float("inf")
        res=window[k-1]-window[l]

        for i in range(k,len(nums)):
            window.append(nums[i])
            window.pop(l)

            res=min(res,window[k-1]-window[l])
        
        return res

