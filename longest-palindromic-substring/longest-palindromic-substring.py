class Solution:
    def longestPalindrome(self, s: str) -> str:


        res=""
        resm=0

        isOdd = len(s)%2
        print(isOdd)
        for i in range(len(s)):
            l=i
            r=i

            while l>=0 and r<len(s) and s[l]==s[r]:

                # print(l,r)
                if r-l+1>resm:
                    resm=r-l+1
                    res=s[l:r+1]

                l=l-1
                r=r+1
                # print(l,r)
                # print('---')

            l=i
            r=i+1

            while l>=0 and r<len(s) and s[l]==s[r]:

                # print(l,r)
                if r-l+1>resm:
                    resm=r-l+1
                    res=s[l:r+1]

                l=l-1
                r=r+1
                # print(l,r)
                # print('---')

        return res
            