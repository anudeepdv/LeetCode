class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        st = collections.deque()
        r=deque()
        for i in s:
            if i == ')' and st:
                st.pop()
            elif i==')':
                r.append(i)
            elif i=='(':
                st.append(i)

        print(r,st)

        return len(st)+len(r)