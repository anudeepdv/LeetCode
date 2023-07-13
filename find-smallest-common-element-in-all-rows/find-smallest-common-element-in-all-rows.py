class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        m=collections.defaultdict(int)
        for r in mat:
            for i in r:
                m[i]+=1

        res=float('inf')

        for i in m:
            if m[i]==len(mat):
                res=min(res,i)

        return res if res !=float('inf') else -1
