class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        nmap = Counter(t)
        need = len(nmap)

        hmap = collections.defaultdict(int)
        have =0

        res=math.inf
        besl , besr = 0,0

        for r in range(len(s)):

            if s[r] in nmap:
                hmap[s[r]]+=1
                if hmap[s[r]]==nmap[s[r]]:
                    have+=1

            while have==need:

                if r-l-1<res:
                    res=r-l-1
                    besl=l
                    besr=r
                
                if s[l] in nmap:
                    hmap[s[l]]-=1
                    if hmap[s[l]]<nmap[s[l]]:
                        have-=1

                l+=1

        return "" if res==math.inf else s[besl:besr+1]

        