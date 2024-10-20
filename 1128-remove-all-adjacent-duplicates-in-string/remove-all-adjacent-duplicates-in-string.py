class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        q= deque()

        for i in s:
            if q and i ==q[-1]:
                q.pop()
            else:
                q.append(i)

        return ''.join(q)