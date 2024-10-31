class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        l = [i%k for i in arr]
        c = Counter(l)
        for a in l:
            b = (k-a)%k

            if a==b:
                if c[a]%2==1:
                    return False
            else:
                if c[a]!=c[b]:
                    return False


        return True
