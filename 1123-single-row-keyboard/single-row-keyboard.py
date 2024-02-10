class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        cur = 0
        tot =0
        for i in word:
            ind= keyboard.find(i)
            tot+=abs(ind-cur)
            cur = ind
        return tot
        