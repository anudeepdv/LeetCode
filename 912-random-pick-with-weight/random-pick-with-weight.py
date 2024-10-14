class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[]
        total=0
        for i in w:
            total+=i
            self.prefix.append(total)
        self.total=total

    def pickIndex(self) -> int:
        
        l= 0 
        r=len(self.prefix)-1

        rand =  random.random()*self.total
        while l<r:

            m = (l+r)//2

            if rand>self.prefix[m]:
                l=m+1
            else:
                r=m

        return l
