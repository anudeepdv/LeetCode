class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m = len(words)

        for i in range(m):
            n = len(words[i])
                
            for j in range(n):
                if j >= m or len(words[j]) <= i or words[i][j] != words[j][i]:
                    return False


        return True