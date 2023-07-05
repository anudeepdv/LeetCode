class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        l=0
        res=0
        hashmap=collections.defaultdict(int)
        for r in range(len(s)):
            hashmap[s[r]]+=1

            while len(hashmap)==3:
                hashmap[s[l]]-=1
                if hashmap[s[l]]==0:
                    del hashmap[s[l]]
                l=l+1

            res=max(res,r-l+1)

        return res
