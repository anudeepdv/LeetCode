class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first = strs[0]

        res=''
        
        for i in range(len(first)):
            for j in range(1,len(strs)):
                word = strs[j]
                if i ==len(word) or word[i]!=first[i]:
                    return res

            res+=first[i]

        return res