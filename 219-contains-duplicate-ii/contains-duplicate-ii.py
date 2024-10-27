class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        m= set()

        for i in range(len(nums)):
            if nums[i] in m:
                return True
            m.add(nums[i])
            if i>=k:
                m.remove(nums[i-k])

        return False