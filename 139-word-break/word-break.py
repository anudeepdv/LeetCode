class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n= len(s)

        w= set(wordDict)

        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(i-1,-1,-1):
                if s[j:i] in w:
                    if dp[j]:
                        dp[i]=1


        return dp[-1]

        