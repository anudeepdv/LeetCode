class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        d=collections.defaultdict(list)

        for i , val in enumerate(s):
            d[val].append(i)

        res=0
        for i in d:

            if len(d[i])>=2:
                l= d[i][0]
                r=d[i][-1]

                res+=len(list(set(s[l+1:r])))


        return res


        