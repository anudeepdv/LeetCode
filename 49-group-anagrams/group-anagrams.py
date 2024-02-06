class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s=collections.defaultdict(list)

        for i in strs:

            n=[0 for i in range(26)]
            for ch in i:
                n[ord(ch)-97]+=1
            s[tuple(n)].append(i)

        return s.values()
        


        