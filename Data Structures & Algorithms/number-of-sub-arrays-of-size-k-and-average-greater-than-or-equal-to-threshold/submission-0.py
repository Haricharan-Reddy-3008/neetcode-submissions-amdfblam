class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        count=0

        for r in range(k,len(arr)+1):
            summ=sum(arr[l:r])
            avg=summ/k
            if avg>=threshold:
                count+=1
            l+=1
        
        return count

        