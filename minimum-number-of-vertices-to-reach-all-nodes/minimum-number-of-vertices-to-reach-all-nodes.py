class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        seta=set()
        setb=set()
        for i in edges:
            seta.add(i[0])
            seta.add(i[1])
            setb.add(i[1])


        print(seta)
        print(setb)

        return seta-setb
