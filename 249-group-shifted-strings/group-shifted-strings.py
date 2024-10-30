class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strings:
            first = ord(s[0])%26
            key = [(ord(i)-first)%26 for i in s]
            res[tuple(key)].append(s)

        return list(res.values())

