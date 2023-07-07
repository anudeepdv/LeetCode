class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def fun(b):
            l=0
            hashMap=collections.defaultdict(int)
            res=0
            for r in range(len(answerKey)):
                hashMap[answerKey[r]]+=1

                while hashMap[b]>k:
                    hashMap[answerKey[l]]-=1
                    l=l+1
                res=max(res,r-l+1)
            return res

        return max(fun('F'),fun('T'))
