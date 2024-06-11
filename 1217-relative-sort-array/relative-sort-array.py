class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        c= Counter(arr1)

        res= []

        for i in arr2:
            if i in c:
                for x in range(c[i]):
                    res.append(i)
                del c[i]

        for i in c:
            for x in range(c[i]):
                    res.append(i)


        return res