class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        nmap = Counter(t)
        need = len(nmap)

        hmap = collections.defaultdict(int)
        have =0

        res=math.inf
        besl , besr = 0,0
        for  r in range(len(s)):
            if s[r] in nmap:
                hmap[s[r]]+=1
                if hmap[s[r]]==nmap[s[r]]:
                    have+=1
            
            while have==need:
                # print(hmap,nmap)
                if r-l+1<res:
                    besl = l
                    besr=r
                    res=r-l+1
                    print(res,"res")
                if s[l] in nmap:
                    hmap[s[l]]-=1
                    if hmap[s[l]]<nmap[s[l]]:
                        have-=1
                        # print("Have",have)

                l+=1

        return s[besl:besr+1] if res!=math.inf else ""
                    
                
