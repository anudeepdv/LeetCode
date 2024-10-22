class Solution:
    def reverseWords(self, s: str) -> str:
        
        q = collections.deque()

        l= 0

        

        r=l

        for r in range(len(s)):
            if s[r]==" ":
                print(l,r)
                if s[l:r+1]==" ":
                    l=r+1
                else:
                    q.appendleft(s[l:r])
                    l=r+1

        if s[l:r+1]!='':

            q.appendleft(s[l:r+1])

        return ' '.join(q)
            

        print(q)

                
