class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        c= collections.Counter(nums)

        l = sorted(list(set(nums)))
        print(l)
        r1=0 
        r2=0

        for i,n in enumerate(l):

            cur = n*c[n]
            if i >0 and l[i]==l[i-1]+1:
                temp = r2
                r2=max(cur+r1,r2)
                r1=temp
            else:
                temp=r2
                r2= cur+r2
                r1=temp

        return r2
