class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        counter = Counter(ages)

        def possible(x,y):
            if y<= 0.5*x +7:
                return False
            if y>x:
                return False

            return True

        req= 0

        for x,num_x in counter.items():
            for y,num_y in counter.items():
                if possible(x,y):

                    if x==y:
                        req+=num_x*(num_x-1)
                    else:
                        req+=num_x*num_y

        return req
