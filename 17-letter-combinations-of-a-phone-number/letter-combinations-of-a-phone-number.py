class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        d= {
            "2" : "abc",
             "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"
        }
        n = len(digits)
        if digits=="":
            return []
        res=[]
        def dfs(i,cur):
            if i ==n:
                res.append(cur)
                return
            
            vals = d[digits[i]]

            for j in vals:
                dfs(i+1,cur+j)
        
        dfs(0,"")

        return res