class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        h=len(people)-1
        res=0
        while l<=h:
            if people[l]+people[h]<=limit:
                res+=1
                l=l+1
                h=h-1
            else:
                res+=1
                h=h-1
        return res
