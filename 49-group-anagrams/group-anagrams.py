class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        print(ord('z'),122-97)

        d=collections.defaultdict(list)
        for s in strs:
            val = [0]*26
            for  i in s:
                val[ord(i)-97]+=1
            
            d[tuple(val)].append(s)

        print(d.values())
        return list(d.values() )           
