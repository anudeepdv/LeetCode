class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        for s in strings:
            x = ord(s[0]) % 26
            ans[tuple((ord(c) - x) % 26  for c in s)].append(s)
            print(ans)
        return ans.values()