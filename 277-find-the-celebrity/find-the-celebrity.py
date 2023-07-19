# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        potceleb= 0

        for i in range(n):
            if(knows(potceleb,i)):
                potceleb=i
        
        print(potceleb)

        for j in range(n):

            if potceleb==j:
                continue
            if knows(potceleb,j) or not knows(j,potceleb):
                return -1
        return potceleb
