class SnapshotArray:

    def __init__(self, length: int):
        
        self.snapId=0
        self.indexHist={}

        for i in range(length):
            self.indexHist[i]=[(0,0)]


    def set(self, index: int, val: int) -> None:
        self.indexHist[index].append((self.snapId,val))

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:

        hist =  self.indexHist[index]
        l=0
        r=len(hist)-1
        res=0
        while l<=r:

            m=(l+r)//2
            if hist[m][0]<=snap_id:
                res=hist[m][1]
                l=m+1
            else:
                r=m-1

        return res



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)