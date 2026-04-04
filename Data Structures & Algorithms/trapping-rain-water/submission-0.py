class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        res=0

        for i in range(1,n-1):
            wtr=min(max(height[0:i]),max(height[i:]))-height[i]
            if wtr>0:
                res+=wtr
        return res
        