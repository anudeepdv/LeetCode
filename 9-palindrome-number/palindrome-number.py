class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False

        rev =0
        y=x
        while x:
            rev=rev*10 + x%10
            x=x//10

        return rev==y