class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res  = [0]*len(temperatures)

        stack = collections.deque()

        for i, val in enumerate(temperatures):
            
            while stack and stack[-1][0]<val:
                popv,popi = stack.pop()
                res[popi]=i-popi
            stack.append((val,i))
        
        return res