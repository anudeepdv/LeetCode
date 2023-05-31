class Twitter:

    def __init__(self):
        self.followerMap=collections.defaultdict(set)
        self.tweetmap=collections.defaultdict(list)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count-=1
        self.tweetmap[userId].append([self.count,tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:

        res=[]
        h=[]

        ids = [i for i in self.followerMap[userId]]
        ids.append(userId)

        for i in ids:
            if i in  self.tweetmap:
                index= len(self.tweetmap[i])-1 
                h.append([ self.tweetmap[i][-1][0], self.tweetmap[i][-1][1],i,index-1])

        heapq.heapify(h)
        i=0
        while h and len(res)<10:
    
            countID,tweetId, PopedUserId, ind = heapq.heappop(h)
            res.append(tweetId)
            if ind>=0:
                heapq.heappush(h,[self.tweetmap[PopedUserId][ind][0],self.tweetmap[PopedUserId][ind][1],PopedUserId,ind-1])
                 
           

        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
      
            self.followerMap[followerId].add(followeeId)
        

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)