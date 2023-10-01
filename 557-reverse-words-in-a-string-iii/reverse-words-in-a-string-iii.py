class Solution:
    def reverseWords(self, s: str) -> str:
        
        l = s.split(' ')
        r= [i[::-1] for i in l]
        return ' '.join(r)