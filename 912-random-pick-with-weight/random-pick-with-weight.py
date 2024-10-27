class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[]
        self.total=0

        for i in w:
            self.total+=i
            self.prefix.append(self.total)
        

    def pickIndex(self) -> int:

        rand = random.random()*self.total

        l=0
        r=len(self.prefix)-1

        res=0
        while l<=r:
            m = (l+r)//2
            if rand<=self.prefix[m]:
                res= m
                r=m-1
            else:
                l=m+1

        return res

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()