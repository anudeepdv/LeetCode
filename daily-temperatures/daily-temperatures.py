class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res=[0]*len(temperatures)
        q=collections.deque()

        for i,num in enumerate(temperatures):
            while q and q[-1][0]<num:
                top,j = q.pop()
                res[j]=i-j

            q.append([num,i])

        return res
