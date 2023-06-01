class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        d= {
            "2" : "abc",
             "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"
        }
        n = len(digits)
        if digits=="":
            return
        

        def dfs(i,s):
            print(i)
            if i == n:
                print(s)
                res.append(s)
                return

            
            alpha = d[digits[i]]

            for a in alpha:
                dfs(i+1,s+a)

        dfs(0,'')
        return res
