class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        c = Counter([v%k for v in arr])

        print(c)
        for key in c:
            other_key = (k -key)%k
            print(key,other_key, c[key],c[other_key])
            if key == other_key:
                if c[key]%2!=0:
                    return False
            else:
                if c[key]!=c[other_key]:
                    return False

        return True