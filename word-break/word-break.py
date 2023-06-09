class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word= set(wordDict)
        dp = [False for i in range(n+1)]
        dp[0]=True
        for i in range(1,n+1):
            for j in range(i-1,-1,-1):
               
        
                if s[j:i] in word:
                    if dp [j]:
                        dp[i]=True
                        break

        

       

        
       
        return dp[-1]

