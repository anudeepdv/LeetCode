class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i ,val in enumerate(words):
            if val==val[::-1]:
                return val
        return ""