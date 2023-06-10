class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        lo = 1
        high = maxSum

        rr = n-index-1
        ll=index
        res=0
        while (lo<=high):

            mid = (lo+high)//2

            curSum = mid

            m=mid-1
            rsum=0
            lsum=0
            if rr!=0:

                if  rr>=m:
                    rsum = (m*(m+1)//2) +(rr-m)*1
                else:
                    rsum = (m*(m+1)//2) - (m-rr)*(m-rr+1)//2

            if ll!=0:

                if  ll>=m:
                    lsum = (m*(m+1)//2) +(ll-m)*1
                else:
                    lsum = (m*(m+1)//2) - (m-ll)*(m-ll+1)//2

            curSum+=lsum+rsum
            print(rsum,lsum,mid,curSum,maxSum)
            if curSum<=maxSum:
                res=mid
                lo=mid+1
            else:
                high=mid-1


        return res


            

