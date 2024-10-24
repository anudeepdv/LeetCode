class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        hayN= len(haystack)
        needleN = len(needle)

        for i in range(0,hayN-needleN+1):
            if haystack[i:i+needleN]==needle:
                return i

        return -1