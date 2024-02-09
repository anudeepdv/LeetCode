class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
      
        len_nums = len(nums)
      
        if len_nums < 2:
            return nums

     
        nums.sort()


        dp = [1] * len_nums
     
        previous_indx = [-1] * len_nums

        max_len = 1 
        max_indx = 0

     
        for i in range(1, len_nums):
        
            for j in range(i):
              
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                 
                    dp[i] = dp[j] + 1
                    previous_indx[i] = j
                  
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_indx = i

        subset = []
        while max_indx != -1:
            subset.append(nums[max_indx])
            max_indx = previous_indx[max_indx]

        return subset[::-1]