class Twitter:

    def __init__(self):
        self.tweetMap = collections.defaultdict(list)
        self.followMap = collections.defaultdict(set)
        self.count =0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        self.followMap[userId].add(userId)

        h = []

        for iid in self.followMap[userId]:
            index = len(self.tweetMap[iid])-1
            if index>=0:
                h.append((self.tweetMap[iid][index][0],self.tweetMap[iid][index][1],iid,index-1))
        
        heapify(h)
        k=10
        res=[]
        while h and k:
            c,tid,iid,index=heappop(h)
            res.append(tid)
            if index>=0:
                heappush(h,(self.tweetMap[iid][index][0],self.tweetMap[iid][index][1],iid,index-1) )
            k-=1
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)