class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        hashMap = {}


        for i,n in enumerate(nums):
            if n in hashMap:

                for vals in hashMap[n]:

                    if abs(i-vals)<=k:
                        return True
                hashMap[n].append(i)

            else:
                 hashMap[n]=[i]

        return False
                    