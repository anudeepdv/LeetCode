class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i,val in enumerate(nums):
            if val:
                self.pairs.append((i,val))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        a,b = self.pairs, vec.pairs
        i,j=0,0
        res=0
        while i<len(a) and j<len(b):
            if a[i][0]==b[j][0]:
                res+=a[i][1]*b[j][1]
                i+=1
                j+=1
            elif a[i][0]<b[j][0]:
                i+=1
            else:
                j+=1

        return res

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)