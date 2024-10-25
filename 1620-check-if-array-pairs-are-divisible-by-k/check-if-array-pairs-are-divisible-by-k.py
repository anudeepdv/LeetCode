class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        c=Counter([i%k for i in arr])

        for x in c:

            other_key = (k-x)%k

            if other_key!=x:
                if c[other_key]!=c[x]:
                    return False

            else:
                if c[other_key]%2!=0:
                    return False

        return True