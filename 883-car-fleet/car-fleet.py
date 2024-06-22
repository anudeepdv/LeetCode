class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        res = [target - i for i in position]

        z = list(zip(res,speed))

        z.sort(key = lambda x:x[0])

        r =[]

        for i in z:
            rem = i[0]/i[1]

            if r:
                if rem <= r[-1]:
                    continue
                else:
                    r.append(rem) 
            else:
                r.append(rem)

        return len(r)

        