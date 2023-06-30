class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        r=0
        l=0
        m=list(s)
        n=len(s)
        for i in range(len(shift)):
            if shift[i][0] == 0:
                l+=shift[i][1]
            else:
                r+=shift[i][1]
        print(r,l)
        if r-l>0:
            for i in range((r-l)%n):
                print(m)
                m.insert(0,m.pop())
        if l-r>0:
            for i in range(l-r):
                m.append(m.pop(0))

        return ''.join(m)
