class SnapshotArray:

    def __init__(self, length: int):
        self.map ={}
        self.snapid = 0

        for i in range(length):
            self.map[i]=[(0,0)]

    def set(self, index: int, val: int) -> None:
        self.map[index].append((val,self.snapid))
        

    def snap(self) -> int:
        self.snapid+=1
        return self.snapid -1
        

    def get(self, index: int, snap_id: int) -> int:

        targetList = self.map[index]
        l=0
        r= len(targetList)-1
        res=0
        while l<=r:

            m = (l+r)//2
            if targetList[m][1]<=snap_id:
                res=targetList[m][0]
                l=m+1
            else:
                r=m-1

        return res


        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)