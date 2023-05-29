class TimeMap:

    def __init__(self):
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append([value,timestamp])
        else:
            self.dict[key]=[[value,timestamp]]


    def get(self, key: str, timestamp: int) -> str:

        if key in self.dict:
            valuesList = self.dict[key]
            # print(valuesList)
            res=''

            l=0
            r=len(valuesList)-1

            while l<=r:
                m=(l+r)//2
                # print(timestamp,valuesList[m][1])
                if valuesList[m][1]<=timestamp:
                    # print(valuesList[m][0])
                    res=valuesList[m][0]
                    l=m+1
                else:
                    r=m-1

            return res


        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)