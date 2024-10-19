class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        c=0
        f=1
        for i in range(len(digits)-1,-1,-1):

            val = digits[i]+f+c
            f=0
            
            c=val//10
            val=val%10
            digits[i]=val

        if c:
            digits.insert(0, c)
        return digits