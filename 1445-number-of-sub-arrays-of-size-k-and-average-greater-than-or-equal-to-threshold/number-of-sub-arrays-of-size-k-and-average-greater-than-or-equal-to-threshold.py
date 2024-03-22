class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        res = sum(arr[:k])
        r=1 if res>=threshold*k else 0
        # print(res)
        for i in range(k,len(arr)):
           
            res=res-arr[i-k]+arr[i]
            # print(res,arr[i-k],arr[i])
            if res>=threshold*k:
                r+=1

        return r


            