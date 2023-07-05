class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        l=0
        res=0
        hashmap=collections.defaultdict(int)
        for r in range(len(s)):
            hashmap[s[r]]+=1

            while len(hashmap)==k+1:
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l=l+1

            res=max(res,r-l+1)

        return res