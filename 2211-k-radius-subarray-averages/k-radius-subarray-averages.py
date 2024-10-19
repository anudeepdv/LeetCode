class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        prefix = []
        s=0

        for i in nums:
            s+=i
            prefix.append(s)
        
        print(prefix)
        res=[-1]*len(nums)
        for i in range(k,len(nums)-k):

            if i-k-1>=0:
                s = prefix[i+k]-prefix[i-k-1]
                print(s//(2*k+1))
                res[i]=s//(2*k+1)
            else:
                s = prefix[i+k]
                print(s//(2*k+1))
                res[i]=s//(2*k+1)


        return res