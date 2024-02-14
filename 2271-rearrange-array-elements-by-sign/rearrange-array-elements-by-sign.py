class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=-1
        n=-1
        for i in range(len(nums)):
            if nums[i]<0 and n==-1:
                n=i
            if nums[i]>0 and p==-1:
                p=i

            if p>-1 and n>-1:
                break

        pfirst=True
        res=[]
        for i in range(len(nums)):
            if pfirst:
                res.append(nums[p])
                p+=1
                while p<len(nums) and nums[p]<0:
                    p+=1

                pfirst=False
            else:
                res.append(nums[n])
                n+=1
                while n<len(nums) and nums[n]>0:
                    n+=1
                pfirst=True
        return res