class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l=0
        
        window = collections.defaultdict(int)
        tmap = Counter(t)
        need = len(tmap)

        have = 0
        besl,besr=0,0
        best = math.inf
        for r in range(len(s)):
            if s[r] in tmap :
                
                window[s[r]]+=1
                if tmap[s[r]]==window[s[r]]:
                    have+=1
                # print(window,have,tmap)
            
            while have == need:
                if r-l+1<best:
                    best = r-l+1
                    besl,besr=l,r

                if s[l] in tmap:
                    window[s[l]]-=1
                    if window[s[l]]<tmap[s[l]]:
                        have-=1

                l=l+1
        # print(best)
        return s[besl:besr+1] if best!=math.inf else ""

