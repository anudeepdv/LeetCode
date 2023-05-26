class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        carry=0
        f=1
        for i in reversed(range(len(digits))):
             s= digits[i]+f+carry
             f=0

             carry= s//10
             val = s%10
             digits[i]=val

        if carry>0:
            digits.insert(0,carry)
        return digits

