class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        
        maxy=0

        hashmap=set()

        for r in range(len(s)):
          
            if s[r] not in hashmap:
                hashmap.add(s[r])
                maxy=max(maxy,r-l+1)
            
            else:
                while s[r] in hashmap:
                  
                    hashmap.remove(s[l])
                    l=l+1
                hashmap.add(s[r])
                maxy=max(maxy,r-l+1)
             
             

        return maxy
