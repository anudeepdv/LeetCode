class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        print(ord("a"))
        print(ord("z"))
        d=collections.defaultdict(list)
        for i in strs:
            l=[0]*26
            for a in i:
                l[ord(a)-97]+=1
            key= tuple(l)
            d[key].append(i)

        return d.values()
            