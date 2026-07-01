from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        if len(s1) > len(s2):
            return False
        
        need =Counter(s1)
        window=Counter(s2[:k])

        if need==window:
            return True
        
        for i in range(k,len(s2)):

            window[s2[i]]+=1


            left=s2[i-k]
            window[left]-=1

            if window[left]==0:
                del window[left]
            
            if window==need:
                return True
            
        return False
        