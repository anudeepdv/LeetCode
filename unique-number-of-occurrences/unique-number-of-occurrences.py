class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        d= collections.Counter(arr)
        print(d)

        return len(d.values())==len(set(d.values()))