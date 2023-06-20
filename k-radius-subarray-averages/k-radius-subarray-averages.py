class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if k==0:
            return nums
        res= [-1 for i in range(len(nums))]

        prefix=[]

        s=0
        for i in nums:
            s=s+i
            prefix.append(s)

        print(prefix)

        for i in range(k,len(nums)-k):

            leftSum=0
            leftSum =prefix[i-1]

            if i-1-k>=0:
               leftSum=leftSum- prefix[i-1-k]

            mid=nums[i]

            rightSum = 0

            if i +k in range(len(nums)):
                rightSum=rightSum+prefix[i+k]-prefix[i]

            s=leftSum+rightSum+mid
            s=s//(2*k+1)
            res[i]=s
        return res
            


