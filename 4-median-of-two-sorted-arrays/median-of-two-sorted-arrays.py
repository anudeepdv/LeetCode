class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A,B = nums1,nums2

        if len(nums2)<len(nums1):
            A,B = B,A

        l =0 
        r= len(A)-1

        n= len(nums1)+len(nums2)
        mid= n//2

        while True:

            i= (l+r)//2
            j = mid-i-2

            Aleft = A[i] if i>=0 else float('-infinity')
            Aright = A[i+1] if i<len(A)-1 else float('infinity')
            Bleft =  B[j] if j>=0 else float('-infinity')
            Bright = B[j+1] if j <len(B)-1 else float('infinity')

            if Aleft<=Bright and Bleft<=Aright:
                if n%2==1:
                    return min(Aright,Bright)

                else:
                     return (max(Aleft,Bleft)+min(Bright,Aright))/2

            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1

        