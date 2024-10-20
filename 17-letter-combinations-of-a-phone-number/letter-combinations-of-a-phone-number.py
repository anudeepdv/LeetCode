class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        d= {
            "2" : "abc",
             "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"
        }
        
        res=[]
        def dfs(i,r):
            if i == len(digits):
                if r!="":
                    res.append(r)
                return
            
            val = digits[i]

            for alpha  in d[val]:
                dfs(i+1,r+alpha)

        dfs(0,"")
        return res
