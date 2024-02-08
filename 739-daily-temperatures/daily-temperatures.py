class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res=[0]*len(temperatures)
        q=collections.deque()


        for i,val in enumerate(temperatures):

            while q and q[-1][0]<val:
                popv, popi = q.pop()
                res[popi]=i-popi

            q.append((val,i))
        return res