class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        res=[-1]
        curMax=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            print(i)
            res.append(curMax)
            curMax=max(arr[i],curMax)

        return reversed(res)